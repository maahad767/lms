from django.contrib.auth import get_user_model
from rest_framework import serializers

from account.models import User

UserModel: User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email', 'first_name', 'last_name')

    def validate(self, data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError("Passwords didn't match.")
        return data

    def create(self, validated_data):
        del validated_data['password2']
        password = validated_data.pop('password1')
        user = UserModel.objects.create_user(**validated_data, password=password)
        return user
