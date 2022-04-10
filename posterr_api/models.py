from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin


class User(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""
    name = models.CharField(max_length=150)
    username = models.CharField(max_length=14, unique=True)
    password = models.CharField(max_length=128)
    email = models.EmailField(max_length=255, unique=True)
    image = models.ImageField(upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name', 'email', 'password']

    def get_username(self):
        """Retrieve username of user"""
        return self.username

    def get_name(self):
        """Retrieve name of user"""
        return self.name

    def get_email(self):
        """Retrieve email of user"""
        return self.email

    def __str__(self):
        """Return string representation of our user"""
        return self.username
