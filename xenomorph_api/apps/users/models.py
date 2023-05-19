from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.db import models

# Create your models here.


class User(AbstractUser):
    email = models.EmailField(blank=False,null=False)
    phonenumber = PhoneNumberField(blank=True, null=True)
    address = models.CharField(max_length=255, null=False, blank=False)



