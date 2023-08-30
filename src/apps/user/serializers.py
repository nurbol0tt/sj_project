from rest_framework import serializers

from src.apps.user.models import User


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("name", "surname", "phone", "password", "role")

    def validate_phone(self, value):
        """
        Validate that the phone number starts with '+996' and is followed by 9 digits.
        """
        if not value.startswith("0"):
            raise serializers.ValidationError("Phone number must start with '0'.")
        if len(value) != 10 or not value[1:].isdigit():
            raise serializers.ValidationError("Phone number must have 10.")
        return value
    
    def create(self, validated_data):
        password = validated_data.pop("password", None)
        instance = self.Meta.model(**validated_data)
        instance.set_password(password)
        instance.save()
        return instance
    

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("name", "surname", "phone",)
