from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, TextInput, Textarea

from .models import Workout


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class WorkoutForm(ModelForm):
    class Meta:
        model = Workout
        fields = ['title', 'week', 'day', 'workout']
        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter workout name'
            }),
            'week': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter a week'
        }),
            'day': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter a day'}),
            'workout': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter description'
            })}
