from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone

from django_smalluuid.models import SmallUUIDField, uuid_default
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractBaseUser, models.Model):
    id = SmallUUIDField(
        default=uuid_default(),
        primary_key=True,
        db_index=True,
        editable=False,
        verbose_name="ID",
    )
    full_name = models.CharField(max_length=100)
    email = models.EmailField(db_index=True)
    phone = PhoneNumberField(blank=True)
    date_joined = models.DateTimeField(default=timezone.now, editable=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False,)

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"

    class Meta:
        ordering = ("-date_joined",)
