from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # 必要に応じてフィールドを追加
    bio = models.TextField(blank=True, null=True)