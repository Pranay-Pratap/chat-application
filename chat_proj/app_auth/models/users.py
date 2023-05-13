from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import UserManager


class users(models.Model):
    """
    User model class
    """

    # object = UserManager()
    # basic user information
    # USERNAME_FIELD = "uid"
    username = models.CharField(
        max_length=128, unique=True
    )
    full_name = models.CharField(
        max_length=200,
        db_column="full_name",
    )
    gender = models.CharField(max_length=10)
    country = models.CharField(max_length=120)
    interest = ArrayField(
        models.CharField(max_length=255), size=10
    )

    email = models.EmailField(
        max_length=75, unique=True
    )
    password = models.CharField(max_length=128)
    phone_number = models.CharField(max_length=20)
    is_active = models.BooleanField(
        default=True,
        help_text=(
            "Designates whether this user should be treated as "
            "active. Unselect this instead of deleting accounts."
        ),
    )
    is_connected = models.BooleanField(
        default=False,
        help_text=(
            "Designates whether this user is connected to the chat server"
        ),
    )
    last_login = models.DateTimeField(blank=True, null=True)
    

    class Meta:
        app_label = "app_auth"
        db_table = "users"
