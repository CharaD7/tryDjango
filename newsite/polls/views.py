from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Question


# Create your views here.
def index(request):
    last_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {
        "last_question_list": last_question_list,
    }
    return render(request, "polls/index.html", context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})


def results(request, question_id):
    response = f"You're looking at the results of question {question_id}."
    return HttpResponse(response)


def vote(request, question_id):
    return HttpResponse(f"You're voting on question {question_id}.")
