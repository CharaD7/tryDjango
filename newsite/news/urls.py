from django.urls import path
from . import views

urlpatterns = [
    path("news/news", views.news, name="news")
]
