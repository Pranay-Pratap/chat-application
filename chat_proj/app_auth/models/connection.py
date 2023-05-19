from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import UserManager


class connection_user(models.Model):
    """A connection to make sure only one to one connection is active at a time for a user"""

    # object = UserManager()
    # basic user information
    # USERNAME_FIELD = "uid"
    username = models.CharField(max_length=128, unique=True)
    connected_username = models.CharField(max_length=128, unique=True)
    is_active = models.BooleanField(max_length=128, default=False)

    class Meta:
        app_label = "app_auth"
        db_table = "connection"
