from django.contrib import admin
from .models import Leaderboard, GameBoards
# Register your models here.

admin.site.register(Leaderboard)    # allows us to edit leaderboard from the admin site.
admin.site.register(GameBoards)     # allows us to edit game boards from the database