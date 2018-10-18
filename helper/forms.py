from django import forms
from django.contrib.auth.models import User

from helper.models import Exercise

LEVELS = (
        (1, 'Początkujący'),
	    (2, 'Średniozaawansowany'),
	    (3, 'Zaawansowany'),
	)

QUANTITY_OF_EXERCISES = (
        (3, '3'),
        (4, '4'),
	    (5, '5'),
	    (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10, '10'),

	)

PARTS = (
        (1, 'Ręce'),
	    (2, 'Nogi'),
	    (3, 'Core'),
	)
QUANTITY = (
        (2, '2'),
	    (3, '3'),
	    (4, '4'),
        (5, '5'),
	)
PERIOD = (
        (1, 'Tydzień'),
	    (2, 'Miesiąc'),
	)
class UserForm(forms.ModelForm):
    #login = forms.CharField(max_length=64)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model=User
        fields = ['username', 'email', 'password']

class LoginForm(forms.ModelForm):
    #login = forms.CharField(max_length=64)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model=User
        fields = ['username', 'password']

class SingleWorkoutForm(forms.Form):
    poziom = forms.ChoiceField(choices=LEVELS)
    kategoria = forms.ChoiceField(choices=PARTS)
    ilość_ćwiczeń = forms.ChoiceField(choices=QUANTITY_OF_EXERCISES)
    drążek = forms.BooleanField(required=False)
    poręcze = forms.BooleanField(required=False)

#forms.MultipleChoiceFieldChoiceField

class WorkoutForm(forms.Form):
    level = forms.ChoiceField(choices=LEVELS)
    weekly_quantity = forms.ChoiceField(choices=QUANTITY)
    period = forms.ChoiceField(choices=PERIOD)

class AddExerciseForm(forms.ModelForm):
    # name = forms.CharField(max_length=64)
    # description = forms.CharField(max_length=255)
    # category = forms.ChoiceField(choices=PARTS)
    # reps = forms.CharField(max_length=64, default="4x 10-12 pwt")
    # level = forms.ChoiceField(choices=LEVELS)
    # #sprzęt do ćwiczeń
    # bar = forms.BooleanField(required=False)
    # parallel_bars = forms.BooleanField(required=False)
    class Meta:
        model=Exercise
        fields = '__all__'

class DeleteExerciseForm(forms.Form):
    id = forms.IntegerField()
