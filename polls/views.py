from typing import Any
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

from .models import Question, Choice
from .forms import NewUserForm


class IndexView(generic.ListView):
    model = Question
    template_name = "index.html"
    context_object_name = "latest_question_list"

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        num_visits = self.request.session.get("num_visits", 0)
        self.request.session["num_visits"] = 1 + num_visits
        context["num_visits"] = num_visits
        return context

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by(
            "-pub_date"
        )[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(LoginRequiredMixin, generic.DetailView):
    model = Question
    template_name = "polls/results.html"

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())


@login_required
def votes(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question_id,)))


def register_request(request):
    form = NewUserForm()
    if request.method == "POST":
        form = NewUserForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("polls:index")

    return render(
        request=request,
        template_name="registration/register.html",
        context={"register_form": form},
    )
