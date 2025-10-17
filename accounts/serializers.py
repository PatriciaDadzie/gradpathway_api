from django.contrib.auth import authenticate
from rest_framework import serializers
from .models import User


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "email", "password", "country_preference")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        username = validated_data.get("username") or validated_data["email"].split("@")[0]
        user = User.objects.create_user(
            username=username,
            email=validated_data["email"],
            password=validated_data["password"],
            country_preference=validated_data.get("country_preference", "")
        )
        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get("email")
        password = data.get("password")

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise serializers.ValidationError({"email": "User with this email does not exist."})

        user = authenticate(username=user.username, password=password)
        if not user:
            raise serializers.ValidationError({"password": "Invalid password."})
        data["user"] = user
        return data
