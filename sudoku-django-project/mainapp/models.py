from django.db import models
from typing import Union

# Create your models here.
class GameBoards(models.Model):
    # An autoincrementing ID column which will be used as primary key is automatically added.
    game_board = models.TextField()
    check_board = models.TextField()
    
    def __str__(self) -> Union[str, int]:
        return self.id

class Leaderboard(models.Model):
    name = models.CharField(max_length=20, default="Player", blank=False)
    time = models.IntegerField()

    def __str__(self) -> str: 
        return ", ".join([self.name, self.time])

