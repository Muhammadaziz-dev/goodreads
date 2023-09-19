from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    profile_picture = models.ImageField(default="default_profile_pic.png")
    phone_number = models.CharField(max_length=9, blank=True, null=True)
