from django.shortcuts import render, redirect

from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.http import HttpResponse

# from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
from . import forms
from . import models
from .forms import RegisterForm, WorkoutForm

from django.views.generic import ListView


@login_required
def index(request):
    return render(request, 'training/index.html', {'title': 'Main page'})


def about_me(request):
    return render(request, 'training/about_me.html', {'title': 'About me'})


def user_login(request):
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                username=cd['username'],
                password=cd['password'],
            )
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Logged In')
                else:
                    return HttpResponse('Not active')
            else:
                return HttpResponse('Wrong credentials')
    else:
        form = forms.LoginForm()
        return render(request, 'training/login.html', {'form': form})


def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()

        return redirect('/')
    else:
        form = RegisterForm()

    return render(response, "registration/register.html", {'form': form})


@login_required
def create(request):
    error = ''
    if request.method == "POST":
        form = WorkoutForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            error = "Entered incorrect data"
    form = WorkoutForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'training/create.html', context)


class MaterialListView(LoginRequiredMixin, ListView):
    queryset = models.Workout.objects.all()
    context_object_name = 'workouts'
    template_name = 'training/index.html'
