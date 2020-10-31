#Defines paths to different views in the mainapp app
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),

    path("leaderboard", views.leaderboard, name="leaderboard")
]