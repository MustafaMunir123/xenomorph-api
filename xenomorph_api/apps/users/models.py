import uuid
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.db import models

# Create your models here.


class User(AbstractUser):
    user_id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    email = models.EmailField(blank=False, null=False, unique=True)
    phonenumber = PhoneNumberField(blank=True, null=True)
    address = models.CharField(max_length=255, null=True, blank=True)



