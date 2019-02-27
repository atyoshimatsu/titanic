from django import forms
from .models import Passenger

class SexChoice(forms.Form):
    choice = forms.ChoiceField(label='sex', choices=Passenger.SEX_CHOICES, initial='male or female')