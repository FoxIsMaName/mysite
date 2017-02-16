from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.utils import timezone
from .models import Question, Choice

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

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
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

def addQues(request):
    return render(request,"polls/addQuest.html",'')

def addChoice(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request,"polls/addChoice.html",{'question': question})

def saveQues(request):
    error_message = 0 
    try:
        question = request.POST['question']
    except:
        error_message = 1
        question = ""
    else:
            q = Question(question_text=question, pub_date=timezone.now())
            q.save()
    return render(request,"polls/saveQuest.html",{"question":question, "error_message":error_message})

def saveChoice(request, question_id):
    error_message = 0 
    try:
        choice = request.POST['choice']
    except:
        error_message = 1
        choice = ""
    else:
            q = Question.objects.get(id=question_id)
            q.choice_set.create(choice_text=choice, votes=0)
    return render(request,"polls/saveChoice.html",{"choice":choice, "error_message":error_message})
