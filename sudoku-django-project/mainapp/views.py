from django.shortcuts import render
from django import http

from utils.classes import BoardsQueue
from utils.exceptions import QueueUnderflowError
from .models import GameBoards

queue = BoardsQueue()

lower, upper = 0, 11    # ID range to load to queue
print(upper, lower, "=======")
for result in GameBoards.objects.filter(id__in=list(range(lower, upper))):
    queue.enqueue([result.id, result.game_board])
else:
    lower, upper = 11, 21
print(upper, lower, "=======")
# Create your views here.
def index(request: http.HttpRequest) -> http.HttpResponse:
    return render(request, "mainapp/index.html", {})

def game(request: http.HttpRequest) -> http.HttpResponse:
    global lower, upper
    try:
        board_id, game_board = queue.dequeue()
    except QueueUnderflowError:
        if upper == 101:        #there are currently only 100 items on the database, so it loops back to the starting.
            lower, upper = 0, 11
        else:
            lower += 10
            upper += 10

        for result in GameBoards.objects.filter(id__in=list(range(lower, upper))):  #loading new tables from database
            queue.enqueue([result.id, result.game_board])
        else:
            lower, upper = upper, upper + 10

        board_id, game_board = queue.dequeue()
    context = {'board_id': board_id, 'game_board': game_board}
    
    return render(request, "mainapp/game.html", context)