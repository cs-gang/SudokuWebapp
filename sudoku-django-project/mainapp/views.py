from django.shortcuts import render, redirect
from django import http
from django.views.decorators.http import require_POST, require_GET
from django.db.models import Max
import json

from utils.classes import BoardsQueue
from utils.exceptions import QueueUnderflowError

from .models import GameBoards, Leaderboard
from .forms import AddToLeaderboardForm


queue = BoardsQueue()

lower, upper = 0, 11    # ID range to load to queue
# filling queue with tables saved on the database
for result in GameBoards.objects.filter(id__in=list(range(lower, upper))):
    queue.enqueue([result.id, json.loads(result.game_board), json.loads(result.check_board)])
else:
    lower, upper = 11, 21

# Create your views here.
@require_GET
def index(request: http.HttpRequest) -> http.HttpResponse:
    return render(request, "mainapp/index.html", {})

@require_GET
def game(request: http.HttpRequest) -> http.HttpResponse:
    global upper, lower
    try:
        board_id, game_board, check_board = queue.dequeue()
    except QueueUnderflowError:
        if upper == 101:        #there are currently only 100 items on the database, so it loops back to the starting.
            lower, upper = 0, 11
        else:
            lower += 10
            upper += 10

        for result in GameBoards.objects.filter(id__in=list(range(lower, upper))):  #loading new tables from database
            queue.enqueue([result.id, json.loads(result.game_board), json.loads(result.check_board)])
        else:
            lower, upper = upper, upper + 10

        board_id, game_board, check_board = queue.dequeue()
    context = {'board_id': board_id, 'game_board': game_board, 'check_board': check_board, 'form': AddToLeaderboardForm()}
    
    return render(request, "mainapp/game.html", context)

def result(request: http.HttpRequest) -> http.HttpResponse:
    if request.method == 'POST':
        form = AddToLeaderboardForm(request.POST)
        if form.is_valid():
            time = form.cleaned_data['time']
            username = form.cleaned_data['username']

        current_worst = Leaderboard.objects.all().aggregate(Max('time'))
        if time < current_worst['time__max']:
            new = Leaderboard(name=username, time=time)
            new.save()

        return redirect('index') 

def leaderboard(request: http.HttpRequest, home: str="") -> http.HttpResponse:
    if home == "lb":
        data = Leaderboard.objects.all().order_by('time')
        formatted_data = [[entry.name, entry.time] for entry in data][:10]
        context = {"data": formatted_data}  # and put that data in context to be passed to the view.
        return render(request, "mainapp/leaderboard.html", context)
    else:
        return redirect("index")

