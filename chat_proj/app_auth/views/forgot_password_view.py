"view to handle forgot password"
from django.contrib.auth import authenticate, login
from django.views.generic import View
from django.shortcuts import render, redirect
from ..models import User

class ForgotPasswordView(View):
    """View to handle forgot password using email
    """

    def post(self, request):
        """Post request to handle forgot password

        Args:
            request (request): request object

        Returns:
            redirect: redirects to login page
        """
        email = request.POST.get("email")
        new_password = request.POST.get("new_password")
        if not email or not new_password:
            return render(request, "forgot_password.html", {"error": "Please fill all the fields"})
        
        user = User.objects.filter(email=email).first()
        if not user:
            return render(request, "forgot_password.html", {"error": "User does not exist"})
        user.set_password(new_password)
        user.save()
        return redirect("login")