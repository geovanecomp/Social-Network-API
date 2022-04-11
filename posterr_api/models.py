from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.validators import RegexValidator


class UserManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self, name, email, username, password=None):
        """Create a new user profile"""

        if not name:
            raise ValueError('User must have a name')
        if not email:
            raise ValueError('User must have an email address')
        if not username:
            raise ValueError('User must have a username')

        email = self.normalize_email(email)
        user = self.model(name=name, email=email, username=username)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, name, email, username, password):
        """Create and save a new superuser"""
        user = self.create_user(name, email, username, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""

    alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')

    name = models.CharField(max_length=150, null=False, validators=[alphanumeric])
    username = models.CharField(max_length=14, unique=True, null=False, validators=[alphanumeric])
    password = models.CharField(max_length=128, null=False)
    email = models.EmailField(max_length=255, null=False, unique=True)
    image = models.ImageField(upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

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


class Post(models.Model):
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    text = models.CharField(max_length=777, null=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
