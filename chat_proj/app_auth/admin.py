from django.contrib import admin

# Register your models here.

from .models.connection import connection_user
from .models.users import users
from .models.connection_users_info import ConnectedUser

admin.site.register(users)
admin.site.register(connection_user)
admin.site.register(ConnectedUser)
