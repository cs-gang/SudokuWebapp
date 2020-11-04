from django.shortcuts import render
from django import http
from django.views.decorators.http import require_http_methods, require_GET
from django.shortcuts import redirect
from django.db.models import Max
import json

from utils.classes import BoardsQueue
from utils.exceptions import QueueUnderflowError
from .models import GameBoards, Leaderboard

# queue initialization 
queue = BoardsQueue()

lower, upper = 0, 11    # ID range to load to queue
# fillinf queue with tables saved on the database
for result in GameBoards.objects.filter(id__in=list(range(lower, upper))):
    queue.enqueue([result.id, json.loads(result.game_board), json.loads(result.check_board)])
else:
    lower, upper = 11, 21


# Create your views here.
@require_GET
def index(request: http.HttpRequest) -> http.HttpResponse:
    return render(request, "mainapp/index.html", {})

@require_http_methods(['GET', 'POST'])
def game(request: http.HttpRequest) -> http.HttpResponse:
    if request.method == 'GET':
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
        context = {'board_id': board_id, 'game_board': game_board, 'check_board': check_board}
        
        return render(request, "mainapp/game.html", context)



def result(request: http.HttpRequest) -> http.HttpResponse:
        """username = request.GET['username']
        time = int(request.GET['time'])

        current_worst = Leaderboard.objects.all().aggregate(Max('time'))

        if time < current_worst['time__max']:
            new = Leaderboard(name=username, time=time)
            new.save()"""
        print(request.GET)
        return redirect('') 