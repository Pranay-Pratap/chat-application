"View to handle signup."

from django.contrib.auth import authenticate, login
from ..models import User
from django.views.generic import View
from django.shortcuts import render, redirect


class SignupView(View):
    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")
        email = request.POST.get("email")
        if not username or not password or not email:
            return render(request, "signup.html", {"error": "Please fill all the fields"})
        if User.objects.filter(username=username).exists():
            return render(request, "signup.html", {"error": "Username already exists"})
        if User.objects.filter(email=email).exists():
            return render(request, "signup.html", {"error": "Email already exists"})
        user = User.objects.create_user(username=username, password=password, email=email)
        user.save()
        return redirect("login")

