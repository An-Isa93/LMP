from django.urls import path

from . import views

app_name = "polls"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
    path("question/",views.question_view,name="question"),
    path("success/",views.question_view,name="question"),
    path("<int:question_id>/choice/",views.choice_view, name="choice")
]