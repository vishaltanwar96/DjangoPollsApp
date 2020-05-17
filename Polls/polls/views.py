from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import Question, Choice


def index(request: HttpRequest) -> HttpResponse:
    recent_ten_questions = Question.objects.all().order_by('-created_at')[:10]
    return render(
        request=request,
        template_name='polls/index.html',
        context={'recent_ten_questions': recent_ten_questions}
    )


def detail(request: HttpRequest, question_id: int) -> HttpResponse:
    question = Question.objects.get(pk=question_id)
    return render(
        request=request,
        template_name='polls/detail.html',
        context={'question': question}
    )


def result(request: HttpRequest, question_id: int) -> HttpResponse:
    question = Question.objects.get(pk=question_id)
    return render(
        request=request,
        template_name='polls/result.html',
        context={'question': question}
    )


def vote(request: HttpRequest, question_id: int) -> HttpResponse:
    pass
