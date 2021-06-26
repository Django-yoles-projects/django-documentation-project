from django.utils import timezone
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.urls import reverse
from django.views import generic

from .models import Question, Choice


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


def index_f(request):
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


def detail_f(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results_f(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_questions'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.filter(
            published_date__lte=timezone.now()
        ).order_by('-published_date')[:5]

        # return Question.objects.filter(published_date__lte=timezone.now().timestamp()).order_by('-published_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(published_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'
