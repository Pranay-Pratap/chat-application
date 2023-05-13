import random
import sys

from django.shortcuts import render

sys.path.append("..")
from app_auth.models import users


def main_view(request):
    """
    Get user from request and find the related user with the same interests
    If no related user found then find the random user

    Return: The related user and username to the template
    """
    username = request.GET['username']
    if username is None:
        return render(request,'main.html', {"message" : "Username is required"})
    
    user = users.objects.get(username=username)
    interest = user.interest
    related_user =  users.objects.filter(interest__overlap=interest,is_active = True, is_connected = False).exclude(username= username).values().first()
    if related_user is None:
        related_user = random.choice(list(users.objects.filter(is_connected = False, is_active= True).exclude(username= username).values()))
    
    return render(request,'main.html', {"related_user" : related_user, "username":username})