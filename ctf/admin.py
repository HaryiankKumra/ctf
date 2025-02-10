from django.contrib import admin
from .models import Team, Player, Question, Leaderboard

admin.site.register(Team)
admin.site.register(Player)
admin.site.register(Question)
admin.site.register(Leaderboard)