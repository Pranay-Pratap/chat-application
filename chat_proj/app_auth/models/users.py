from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.forms import CharField


class User():
    """
    User model class
    """

    # basic user information
    username = models.CharField(
        ("Stores the username of the user"), max_length=128, unique=True
    )
    name = models.CharField(
        ("Stores the name of the user"),
        max_length=200,
        blank=True,
        db_column="first_name",
    )
    gender = models.CharField(("Stores the gender of the user"), max_length=10)
    country = models.CharField(("Stores the country of the user"), max_length=120)
    intrest = ArrayField(
        CharField(max_length=255), size=10, default=list, blank=True, null=True
    )

    email = models.EmailField(
        ("Stores the email of the user"), max_length=75, unique=True
    )
    password = models.CharField(("Stores the password of the user"), max_length=128)
    phone_number = models.CharField(max_length=20, blank=True)
    is_active = models.BooleanField(
        ("Stores whether the user is active or not"),
        default=True,
        help_text=(
            "Designates whether this user should be treated as "
            "active. Unselect this instead of deleting accounts."
        ),
    )
    
    class Meta:
        app_label = "app_auth"
        db_table = "user"