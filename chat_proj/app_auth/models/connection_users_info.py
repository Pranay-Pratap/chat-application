
from django.db import models

class ConnectedUser(models.Model):

    username  = models.CharField(max_length=128, unique=True)
    connected_username = models.CharField(max_length=128, unique=True)
    is_active = models.BooleanField(max_length=128, default=False)

    class Meta:
        app_label = "app_auth"
        db_table = "connected_users"