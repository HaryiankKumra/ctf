from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
from .models import Team, Question, Leaderboard
import json

def login(request):
    if request.method == 'POST':
        team_name = request.POST.get('team_name')
        team_code = request.POST.get('team_code')
        try:
            team = Team.objects.get(team_name=team_name, team_code=team_code)
            request.session['team_id'] = str(team.id)  # MongoDB uses ObjectId
            return redirect('questions')
        except Team.DoesNotExist:
            messages.error(request, 'Invalid team name or code')
    return render(request, 'ctf/login.html')


def questions(request):
    if 'team_id' not in request.session:
        return redirect('login')
    
    questions = list(Question.objects.values())  # Convert QuerySet to list of dicts
    return render(request, 'ctf/questions.html', {'questions': json.dumps(questions)})

def leaderboard(request):
    leaderboard = Leaderboard.objects.order_by('-score')
    return render(request, 'ctf/leaderboard.html', {'leaderboard': leaderboard})

def submit_answer(request, question_id):
    if request.method == 'POST':
        data = json.loads(request.body)
        answer = data.get('answer')
        question = Question.objects.get(id=question_id)
        
        if answer == question.answer:
            # Update leaderboard
            team = Team.objects.get(id=request.session['team_id'])
            leaderboard_entry, created = Leaderboard.objects.get_or_create(team=team)
            leaderboard_entry.score += question.points
            leaderboard_entry.save()
            return JsonResponse({'correct': True})
        else:
            return JsonResponse({'correct': False})
    return JsonResponse({'error': 'Invalid request'}, status=400)