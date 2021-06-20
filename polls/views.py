from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from django.template import loader

from .models import Question


def index_no_template(request):
    latest_questions_list = Question.objects.order_by('-published_date')[:5]
    output = ', '.join([q.title for q in latest_questions_list])
    return HttpResponse(f"Hello, You're at the polls index. This is the last questions :<strong>{output} </strong>")


def index_long(request):
    latest_question_list = Question.objects.order_by('-published_date')[:5]
    print("[debug]: ", latest_question_list)
    template = loader.get_template('polls/index.html')
    context = {
        'latest_questions': latest_question_list,
    }
    return HttpResponse(template.render(context, request))


def index(request):
    latest_question_list = Question.objects.order_by('-published_date')[:5]
    context = {
        'latest_questions': latest_question_list,
    }
    return render(request, "polls/index.html", context)


def detail_long(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    response = f"You're looking at the results of question {question_id}."
    return HttpResponse(response)


def vote(request, question_id):
    return HttpResponse(f"You're voting on question {question_id}.")
