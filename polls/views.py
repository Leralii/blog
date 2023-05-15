from django.http import HttpResponse, Http404
from django.shortcuts import render

from polls.models import Question, Choice


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    choices = question.choices.all()
    context = {
        "question": question,
        "choices": choices
    }
    return render(request, "polls/detail.html", context)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)


def homework(request, params):
    context = {
        "fruits":["apple", "orange","lemon"],
        "header":params
    }
    return render(request, "polls/fruits.html", context)
