"views to handle logout"
from django.contrib.auth import logout
from django.views.generic import View
from django.shortcuts import redirect

class Logout(View):
    def get(self, request):
        """Handle logout

        Args:
            request (request): request object
        
        Returns:
            redirect: redirect to login page
        """
        logout(request)
        return redirect("login")