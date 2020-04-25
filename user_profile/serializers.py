from rest_framework.authtoken.models import Token
from rest_framework import serializers
from user_profile.models import User


class UserRegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        user.set_password(validated_data['password'])
        user.save()
        Token.objects.create(user=user)
        return user


class UserPasswordResetSerializer(serializers.Serializer):
    email = serializers.EmailField()


class UserPasswordResetDoneSerializer(serializers.Serializer):
    password = serializers.CharField()
    password2 = serializers.CharField()


class UserPasswordChangeSerializer(serializers.Serializer):
    current_password = serializers.CharField()
    new_password = serializers.CharField()
    new_password2 = serializers.CharField()


class UserSerializer(serializers.HyperlinkedModelSerializer):
    # users = serializers.HyperlinkedRelatedField(many=True, view_name='user_detail', read_only=True)

    class Meta:
        model = User
        # fields = ('url', 'id', 'username', 'email', 'user_type', 'phone_number', 'posts')
        fields = ('id', 'first_name', 'last_name', 'username', 'email', 'phone_number', 'address',
                  'linkedin_profile', 'personal_website')