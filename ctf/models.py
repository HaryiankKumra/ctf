from djongo import models

class Team(models.Model):
    team_name = models.CharField(max_length=100, unique=True)
    team_code = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.team_name

class Player(models.Model):
    team = models.EmbeddedField(model_container=Team)
    player_name = models.CharField(max_length=100)

    def __str__(self):
        return self.player_name

class Question(models.Model):
    DIFFICULTY_CHOICES = [
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard'),
    ]
    title = models.CharField(max_length=200)
    description = models.TextField()
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES)
    points = models.IntegerField()
    answer = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class Leaderboard(models.Model):
    team = models.EmbeddedField(model_container=Team)
    score = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.team.team_name} - {self.score}"