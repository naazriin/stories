from rest_framework import serializers
from django.contrib.auth import get_user_model

from rest_framework.serializers import TokenObtainPairSerializer


User = get_user_model()

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
        ]


class UserObtainAccessSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
            data = super().validate(attrs)

            user_serializer = UserSerializer(self.user)

            data.update(user_serializer.data)
            return data