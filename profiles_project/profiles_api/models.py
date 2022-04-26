from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class UserProfileManager(BaseUserManager):
    """ Helps Django work with our custom user model. """

    def create_user(self, email, name, password=None):
        """Creates a new user profile object."""

        if not email:
            raise ValueError("Users must have an email address.")

        email = self.normalized_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)

        user.save(using=self._db)

        return user

    def create_super_user(self, email, name, password):
        """Creates and saves a new superuser with given details"""

        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """
    Represents a "User Profile" inside our system. 
    """
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        """Django uses this when it needs to convert the object to a string."""
        return self.email

    def get_full_name(self):
        """Use to get user's full name"""
        return self.name