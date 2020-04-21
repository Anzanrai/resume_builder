from django.contrib.auth import authenticate
from django.core.mail import EmailMessage
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import check_password
from django.template.loader import render_to_string

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated

from .tokens import TokenGenerator
from .models import User
from .serializers import UserRegistrationSerializer, UserPasswordResetSerializer, UserPasswordResetDoneSerializer, \
    UserPasswordChangeSerializer


class RegistrationView(generics.CreateAPIView):
    """Create a new user in the system"""
    serializer_class = UserRegistrationSerializer


class LoginUserView(APIView):
    """Login the user in the system"""
    serializer_class = UserRegistrationSerializer

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            return Response({"token": user.auth_token.key})
        else:
            return Response({"error": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)


def send_email(user):
    message = render_to_string('user_profile/password_reset_email.html',{
        'protocol': 'http',
        'domain': 'localhost:8000',
        'uid': str(user.pk),
        'token': TokenGenerator().make_token(user),
    })
    mail_subject = 'Password Reset.'
    to_email = user.email
    email = EmailMessage(mail_subject, message, to=[to_email])
    send = email.send()
    return send


@csrf_exempt
@api_view(['POST'])
def passwordreset_view(request):
    if request.method == 'POST':
        serializer = UserPasswordResetSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            if email != '':
                email = User.objects.get(email=email)
                if not email:
                    return Response(data={'message': "Couldn't found matching email!"})
                else:
                    return Response(send_email(email))
            else:
                return Response(data={'message': 'Empty email provided'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['POST'])
def passwordresetdone_view(request, uid, token):
    if request.method == 'POST':
        user = User.objects.get(pk=uid, auth_token=token)
        serializer = UserPasswordResetDoneSerializer(data=request.POST)
        if serializer.is_valid(request.POST):
            password = serializer.validated_data['password']
            password2 = serializer.validated_data['password2']
            if password == password2:
                user.set_password(password)
                user.save()
                return Response("Password reset done!")
            else:
                return Response("Confirm your password and try again")
        else:
            return Response(serializer.errors)


class PasswordChangeView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = UserPasswordChangeSerializer(data=request.POST)
        if serializer.is_valid():
            current_password = serializer.validated_data['current_password']
            new_password = serializer.validated_data['new_password']
            new_password2 = serializer.validated_data['new_password2']
            if check_password(current_password, request.user.password):
                if new_password == new_password2:
                    request.user.set_password(new_password)
                    request.user.save()
                    return Response("Your password is Successfully changed!")
                else:
                    return Response("New password didn't match!")
            else:
                return Response("Current password Doesn't match with your password!")
        else:
            return Response(serializer.errors)