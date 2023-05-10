"view to handle login"

from django.contrib.auth import authenticate, login
from django.views.generic import View
from django.shortcuts import render, redirect
from ..models import User


class LoginView(View):
    def post(self, request):
        """Handle login

        Args:
            request (request): request object
        
        Returns:
            redirect: redirect to home page
        """
        if request.POST.get("email"):
            email = request.POST.get("email")
        
        if request.POST.get("phone_number"):
            phone_number = request.POST.get("phone_number")

        password = request.POST.get("password")
        if not email and not phone_number:
            return render(request, "login.html", {"error": "Please fill all the fields"})
        if email:
            user = User.objects.filter(email=email).first()
        if phone_number:
            user = User.objects.filter(phone_number=phone_number).first()

        if not user:
            return render(request, "login.html", {"error": "User does not exist"})
        if not user.check_password(password):
            return render(request, "login.html", {"error": "Incorrect password"})
        login(request, user)
        return redirect("home")
    
