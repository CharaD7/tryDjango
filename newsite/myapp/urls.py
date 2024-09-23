from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("dishes/<str:dish>", views.menu_items)
]
