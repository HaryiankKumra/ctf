from django import forms

class LoginForm(forms.Form):
    team_name = forms.CharField(max_length=100)
    team_code = forms.CharField(max_length=50)