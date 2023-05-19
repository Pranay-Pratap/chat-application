import random
import sys

from django.shortcuts import render

sys.path.append("..")
from app_auth.models import users, connection_user
from app_auth.models.connection_users_info import ConnectedUser


def main_view(request):
    """
    Get user from request and find the related user with the same interests
    If no related user found then find the random user

    Return: The related user and username to the template
    """
    username = request.GET['username']
    if username is None:
        return render(request,'main.html', {"message" : "Username is required"})
    
    connected_user = get_connected_user(username)

    if connected_user:
        return render(request,'main.html', {"related_user" : connected_user, "username":username})

    user = users.objects.get(username=username)
    interest = user.interest
    related_user =  users.objects.filter(interest__overlap=interest,is_active = True, is_connected = False).exclude(username= username).values().first()
    if related_user is None:
        related_users = list(users.objects.filter(is_connected = False, is_active= True).exclude(username= username).values())
        if related_users:
            related_user = random.choice(related_users)
        else:
            return render(request,'main.html', {"message" : "No related user found"})
    
    ConnectedUser.objects.create(
        username = username,
        connected_username = related_user['username'],
        is_active = True
    )

    return render(request,'main.html', {"related_user" : related_user, "username":username})


def get_connected_user(username):
    """A connection to make sure only one to one connection is active at a time for a user"""

    connected_username = ConnectedUser.objects.filter(username=username, is_active=True)

    if connected_username.count() > 0:
        connected_username = connected_username[0]
        connected_user = users.objects.filter(username=connected_username.connected_username, is_active=True)
        if connected_user.count() > 0:
            return connected_user[0].__dict__

    connected_username = ConnectedUser.objects.filter(connected_username=username, is_active=True)
    if connected_username.count() > 0:
        connected_username = connected_username[0]
        connected_user = users.objects.filter(username=connected_username.username, is_active=True)
        if connected_user.count() > 0:
            return connected_user[0].__dict__
        
    return None
    
    
