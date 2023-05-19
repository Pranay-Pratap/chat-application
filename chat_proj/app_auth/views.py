from django.conf import settings
from django.contrib import messages
from django.contrib.auth import login, logout
from django.shortcuts import redirect, render

from chat_proj import settings

from .models import users
from .serializers import UserDetailSerializer
from .models.connection_users_info import ConnectedUser


def homeView(request):
    """
    Home page view
    """
    return render(request, "app_auth/base.html")

def signupView(request):
    """
    Signup the user and redirect to Login page
    """
    if request.method == "POST":
        username = request.POST['username']
        phone_number = request.POST['phone_number']
        email = request.POST['email']
        pass1 = request.POST['password']
        pass2 = request.POST['pass2']
        
        if users.objects.filter(username=username):
            messages.error(request, "Username already exist! Please try some other username.")
            return redirect('home')
        
        if users.objects.filter(email=email).exists():
            messages.error(request, "Email Already Registered!!")
            return redirect('home')
        
        if len(username)>20:
            messages.error(request, "Username must be under 20 charcters!!")
            return redirect('home')
        
        if not phone_number.isnumeric() and len(phone_number) != 10:
            messages.error(request, "Phone number is not valid!!")
            return redirect('home')
        
        if pass1 != pass2:
            messages.error(request, "Passwords didn't matched!!")
            return redirect('home')
        
        if not username.isalnum():
            messages.error(request, "Username must be Alpha-Numeric!!")
            return redirect('home')
        data = request.POST.copy()

        data["is_active"] = True
        data["is_connected"] = False
        serializer = UserDetailSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        messages.success(request, "Your Account has been created succesfully!!")
        
        return redirect('login')
    return render(request, "signup.html", {"message":"Successfully Signed up"})

def loginView(request):
    """
    Login the user and redirect to home page
    Set the session for the user

    Request:
            Request data
    
            Request Type: POST
    Response:
            Redirect to home page
    """
    if request.method == "POST":
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        pass1 = request.POST['password']
        
        if users.objects.filter(email=email).exists():
            user = users.objects.get(email=email)
            if user.password == pass1:
                request.session['email'] = email
                messages.success(request, "Successfully Logged in!!")
                # user.backend = settings.AUTHENTICATION_BACKENDS[0]
                login(request, user)
                user.is_active = True
                user.save()
                full_name = user.full_name
                is_active = user.is_active
                username = user.username
                user.is_authenticated = True
                return render(request, "app_auth/base.html", {"full_name":full_name, "is_active":is_active, "username":username})
            else:
                messages.error(request, "Invalid Credentials!!")
                return redirect('login')
        else:
            messages.error(request, "Invalid Credentials!!")
            return redirect('login')
    return render(request, "login.html", {"message":"Successfully Signed up"})

def logoutView(request):
    """
    Logout the user and redirect to home page

    :param request: The request username
    :redirect: The response to redirect to home page
    """
    username = request.GET['username']
    user = users.objects.get(username=username)
    user.is_active = False
    user.save()

    ConnectedUser.objects.filter(username=username).delete()
    ConnectedUser.objects.filter(connected_username=username).delete()

    logout(request)
    messages.success(request, "Successfully Logged out!!")
    return redirect('home')