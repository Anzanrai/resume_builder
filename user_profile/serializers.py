from django.contrib.auth import get_user_model, authenticate
from rest_framework import serializers
from user_profile.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password')
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)



