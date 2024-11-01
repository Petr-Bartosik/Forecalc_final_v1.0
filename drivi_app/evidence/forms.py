from django import forms
from .models import DrevoZaznam

class DrevoZaznamForm(forms.ModelForm):
    class Meta:
        model = DrevoZaznam
        fields = ['nazev', 'delka', 'prumer']
