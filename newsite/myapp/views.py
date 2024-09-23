from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def home(request):
    return HttpResponse("Hello, world. You're on the index page.")


def menuItems(request, dish):
    items = {
        'pasta': 'Pasta is a type of noodle made from the combination of...',
        'falafel': 'Falfel are deep fried patties or balls made from ...',
        'cheesecake': 'Cheesecake is a type of dessert made with...',
    }
    description = items[dish]
    return HttpResponse(f"<h2> {dish} </h2>" + description)
