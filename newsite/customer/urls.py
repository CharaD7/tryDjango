from django.urls import path
from . import views


urlpatterns = [
    path("customer/home", views.home, name="home"),
    path("customer/signup", views.signup, name="signup"),
]
