from django import forms

class AddToLeaderboardForm(forms.Form):
    username = forms.CharField()
    time = forms.IntegerField()