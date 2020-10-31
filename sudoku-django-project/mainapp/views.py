from django.shortcuts import render
from django import http
# Create your views here.

def index(request: http.HttpRequest) -> http.HttpResponse:
    return render(request, "mainapp/index.html", {})

def game(request: http.HttpRequest) -> http.HttpResponse:
    # get board from queue and add it to this context dictionary to be passed to the view file.
    context = {}
    return render(request, "mainapp/game.html", context)