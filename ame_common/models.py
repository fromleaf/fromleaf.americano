from django.db import models
from django.contrib.auth.models import User, BaseUserManager, AbstractBaseUser, PermissionsMixin


class User(models.Model):
    user = models.OneToOneField(User)

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=32)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(null=True)

    def __str__(self):
        return self.name
