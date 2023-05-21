from rest_framework import serializers
from xenomorph_api.apps.users.models import User
from django.contrib.auth.hashers import make_password


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=120)
    password = serializers.CharField(max_length=128)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

    def create(self, validated_data):
        validated_data["password"] = make_password(validated_data.get("password"))
        user = User.objects.create(**validated_data)
        return user

    def update(self, instance, validated_data):
        validated_data["password"] = make_password(validated_data.get("password"))
        user = User.objects.filter(user_id=instance.user_id).update(**validated_data)
        return user