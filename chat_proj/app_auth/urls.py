
from django.contrib import admin
from django.urls import path
from . import views
# from .views import HomeView, LoginView, Logout, ForgotPasswordView, RelatedUserView

urlpatterns = [
    path("home", views.homeView, name="home"),
    path("signup/", views.signupView, name="signup"),
    path("login/", views.loginView, name="login"),
    path("logout/", views.logoutView, name="logout"),
]


