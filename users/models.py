from django.contrib.auth.models import AbstractUser
from django.db import models


class BiblioUser(AbstractUser):
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, default='')
