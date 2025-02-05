"""
This module defines custom user models for the authentication system.
Classes:
    CustomUserManager(BaseUserManager):
        Manager class for CustomUser model with methods to create users and superusers.
    CustomUser(AbstractBaseUser, PermissionsMixin):
        Custom user model that uses email as the unique identifier instead of username.
Methods:
    CustomUserManager.create_user(self, email, username, password=None, **extra_fields):
        Creates and saves a regular user with the given email, username, and password.
    CustomUserManager.create_superuser(self, email, username, password=None, **extra_fields):
        Creates and saves a superuser with the given email, username, and password.
Attributes:
    CustomUser.email (EmailField):
        The email field for the user, which is unique.
    CustomUser.username (CharField):
        The username field for the user, which is unique and has a maximum length of 150 characters.
    CustomUser.is_active (BooleanField):
        Indicates whether the user account is active. Defaults to True.
    CustomUser.is_staff (BooleanField):
        Indicates whether the user has staff privileges. Defaults to False.
    CustomUser.objects (CustomUserManager):
        The manager for the CustomUser model.
    CustomUser.USERNAME_FIELD (str):
        The field used for authentication. Set to 'email'.
    CustomUser.REQUIRED_FIELDS (list):
        A list of the required fields for creating a user. Contains 'username'.
    CustomUser.__str__(self):
        Returns the string representation of the user, which is the email.
"""
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class CustomUserManager(BaseUserManager):
    """
    Custom manager for User model.\n
    Methods:\n
    create_user(email, username, password=None, **extra_fields)
        Creates and saves a User with the given email, username, and password.
    create_superuser(email, username, password=None, **extra_fields)
        Creates and saves a superuser with the given email, username, and password.
    """
    def create_user(self, email, username, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, username, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    """
    CustomUser model that extends AbstractBaseUser and PermissionsMixin.\n
    Attributes:
        email (EmailField): The email address of the user, used as the unique identifier.
        username (CharField): The username of the user, must be unique and have a maximum length of 150 characters.
        is_active (BooleanField): Indicates whether the user's account is active. Defaults to True.
        is_staff (BooleanField): Indicates whether the user can log into the admin site. Defaults to False.
        objects (CustomUserManager): The manager for the CustomUser model.
    Constants:
        USERNAME_FIELD (str): The field used for authentication, set to 'email'.
        REQUIRED_FIELDS (list): A list of fields that are required when creating a user via the createsuperuser command, set to ['username'].
    Methods:
        __str__(): Returns the string representation of the user, which is the email address.
    """
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email