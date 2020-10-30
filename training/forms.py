from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group
from django.forms import ModelForm, TextInput, Textarea, DateTimeInput

from .models import Workout, Comment, Profile


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    group = forms.ModelChoiceField(queryset=Group.objects.all(),
                                   required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'group']


class WorkoutForm(ModelForm):
    class Meta:
        model = Workout
        fields = ['title', 'workout_body', 'user', 'start_time']
        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter workout name'}),
            'workout_body': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter description'
            }),
            'start_time': DateTimeInput(attrs={
                'class': 'form-control'
            })
           }


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'body']




