from django.http import HttpResponse
# response - ответ, request - запрос
# from .models import Question

from django.shortcuts import render
from django.template import loader


def indexnew(request):
    template = loader.get_template("template/polls/index.html")
    context = "Ready html"
    return HttpResponse(template.render(context, request))

def indexht(request):
    return render(request, "index.html")

def index(request):
    return HttpResponse("Hello, world. You're at the pools")


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
