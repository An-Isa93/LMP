from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Question
from .models import Choice
from django.template import loader
from django.http import Http404
from django.views import generic
from django.utils import timezone
from .forms import QuestionForm, ChoiceForm



class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name="latest_question_list"

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[:5]

def question_view(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,"polls/success.html")
    else:
        form=QuestionForm()
    return render(request,"polls/question.html",{'form':form})

def choice_view(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == "POST":
        form = ChoiceForm(request.POST)
        if form.is_valid():
            choice = form.save(commit=False)
            choice.question = question
            choice.save()
            return HttpResponseRedirect(reverse("polls:detail", args=(question_id,)))
    else:
      
        form = ChoiceForm()

    
    return render(request, "polls/choice.html", {"form": form, "question": question})


class DetailView(generic.DetailView):
    model=Question
    template_name="polls/detail.html"

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now()) 

class ResultsView(generic.DetailView):
    model=Question
    template_name="polls/results.html"


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice",
            },
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))

