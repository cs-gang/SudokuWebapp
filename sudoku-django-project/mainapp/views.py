from django.shortcuts import render
from django import http

from mainapp.models import Leaderboard
# Create your views here.

def index(response: http.HttpRequest) -> http.HttpResponse:
    return render(response, "mainapp/index.html", {})
# this whitespace is me trying to avoid merge conflicts later, I'll remove it later ~ anand.








































def leaderboard(request: http.HttpRequest) -> http.HttpResponse:
    data = Leaderboard.objects.all().order_by('time')
    context = {"data": formatted_data}  # and put that data in context to be passed to the view.
    return render(request, "mainapp/leaderboard.html", context)
