from django.urls import path
from . import views

urlpatterns = [
    path("UserProfileRegistration/", views.registerPage, name="register"),
    path("UserProfileRegistration/login", views.loginPage, name="login"),
    path("UserProfileRegistration/logout", views.logoutUser, name="logout"),
    path("UserProfileRegistration/home", views.home, name="home")

]