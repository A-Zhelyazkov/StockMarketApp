from django.contrib.auth import models as auth_models
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from StockMarketApp.users.managers import AppUserManager


class AppUser(auth_models.AbstractUser, auth_models.PermissionsMixin):
    email = models.EmailField(
        null=False,
        blank=False,
        unique=True,
    )

    first_name = models.CharField(_("first name"), max_length=150, blank=True)
    last_name = models.CharField(_("last name"), max_length=150, blank=True)
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = AppUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email


class Profile(models.Model):
    MAX_FIRST_NAME_LEN = 30
    MAX_LAST_NAME_LEN = 30

    first_name = models.CharField(
        max_length=MAX_FIRST_NAME_LEN,
        blank=True,
        null=True
    )

    last_name = models.CharField(
        max_length=MAX_LAST_NAME_LEN,
        blank=True,
        null=True
    )

    date_of_birth = models.DateField(
        blank=True,
        null=True,
    )

    profile_picture = models.URLField(
        blank=True,
        null=True,
    )

    balance = models.IntegerField(
        blank=True,
        null=True,
    )

    user = models.OneToOneField(
        AppUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )
