from django.http import HttpResponse
from django.shortcuts import render

from polls.models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)


def first_view(request, to_print="default"):
    return HttpResponse(f"Hello {to_print}")

def detail(request, question_id):
    # TODO получить вопрос по question_id
    # TODO получить все варианты ответа по вопросу
    # TODO добавить в контекст вопрос и варианты ответа
    # TODO сделать шаблон
    # TODO в шаблоне в заголовок написать название вопроса
    # TODO в список написать варианты ответов

    return HttpResponse("You're looking at question %s." % question_id)

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
