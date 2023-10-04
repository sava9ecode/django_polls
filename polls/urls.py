from django.urls import path

from . import views


app_name = "polls"

urlpatterns = [
    path("", views.QueistionListView.as_view(), name="index"),
    path("<int:pk>", views.QuestionDetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.results, name="results"),
    path("<int:pk>/vote/", views.votes, name="vote"),
]
