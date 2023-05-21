from rest_framework import serializers
from xenomorph_api.apps.tracking.models import (
    Tracks,
    UserFeedback
)
from xenomorph_api.apps.users.api.v1.serializers import UserSerializer


class TrackingSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    traveler = UserSerializer(read_only=True, many=False)
    traveler_id = serializers.CharField(max_length=70)
    origin_location = serializers.CharField(max_length=400, allow_blank=False, allow_null=False)
    origin_date = serializers.DateField(allow_null=False)
    destination_location = serializers.CharField(max_length=400)
    destination_date = serializers.DateField(allow_null=False)
    active = serializers.BooleanField(default=True)

    def create(self, validated_data):
        track = Tracks.objects.create(**validated_data)
        return track


class UserFeedbackSerializer(serializers.Serializer):
    user = UserSerializer(read_only=True, many=False)
    user_id = serializers.UUIDField()
    feedback = serializers.CharField(max_length=400, allow_null=False, allow_blank=False)

    def create(self, validated_data):
        user_feedback = UserFeedback.objects.create(**validated_data)
        return user_feedback


