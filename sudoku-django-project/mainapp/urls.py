#Defines paths to different views in the mainapp app
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),

    path("game", views.game, name="game"),
    path("result/<str:username>/<int:time>", views.result, name="result"),
    path("leaderboard/<home>", views.leaderboard, name="leaderboard")
]
