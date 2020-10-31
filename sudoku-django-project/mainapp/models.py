from django.db import models

# Create your models here.
class GameBoards(models.Model):
    # An autoincrementing ID column which will be used as primary key is automatically added.
    board = models.TextField()

    def __str__(self):
        return self.board

class Leaderboard(models.Model):
    name = models.CharField(max_length=20, default="Player", blank=False)
    time = models.IntegerField()

    def __str__(self):
        return self.name

