from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('questions/', views.questions, name='questions'),
    path('leaderboard/', views.leaderboard, name='leaderboard'),
    path('submit-answer/<str:question_id>/', views.submit_answer, name='submit_answer'),
]