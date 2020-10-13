from django.shortcuts import render
from django import http
# Create your views here.

def index(response: http.HttpRequest) -> http.HttpResponse:
    return render(response, "mainapp/index.html", {})
