import uuid
from django.db import models
from xenomorph_api.apps.users.models import User

# Create your models here.


class UserFeedback(models.Model):
    objects = None
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="feedback_user")
    feedback = models.CharField(max_length=400, null=False, blank=False)


class Tracks(models.Model):
    objects = None
    id = models.UUIDField(editable=False, primary_key=True)
    traveler = models.ForeignKey(User, on_delete=models.CASCADE, related_name="traveler")
    origin_location = models.CharField(max_length=400, blank=False, null=False)
    origin_date = models.DateField(blank=False, null=False)
    destination_location = models.CharField(max_length=400, blank=False, null=False)
    destination_date = models.DateField(blank=False, null=False)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.origin_location} {self.destination_location}"


class Mark(models.Model):
    objects = None
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    track = models.ForeignKey(Tracks, on_delete=models.CASCADE, related_name="mark_track")
    location = models.CharField(max_length=70, null=False, blank=True)

    def __str__(self):
        return self.location
