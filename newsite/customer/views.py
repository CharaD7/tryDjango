from django.shortcuts import render
from django.http import HttpResponse

from .forms import InputForm


# Create your views here.


def signup(request):
    form = InputForm()
    context = {"form": form}
    return render(request, "signup.html", context)
