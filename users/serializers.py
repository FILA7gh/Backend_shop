from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError


class UserValidationSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class UserCreateValidateSerializer(UserValidationSerializer):

    def validate_username(self, username):
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise ValidationError('User already exists!')

    def validate_password(self, password):
        if len(password) < 8:
            raise ValidationError('password is too short!')
        return password


class UserLoginValidateSerializer(UserValidationSerializer):
    pass


class UserConfirmSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = ['id', 'code']
