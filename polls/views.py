from django.views.generic import DetailView, ListView
from django.http import HttpResponse

from .models import Question, Choice


class QueistionListView(ListView):
    model = Question
    template_name = "index.html"

    def get_queryset(self):
        data = Question.objects.order_by("-pub_date")[:5]
        # output = ", ".join([q.question_text for q in data])
        return data


class QuestionDetailView(DetailView):
    model = Question


def results(request, pk):
    return HttpResponse(f"You're looking at the results of question {pk}")


def votes(results, pk):
    return HttpResponse(f"You're voting on question {pk}")
