from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.http import HttpResponse

from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required, permission_required
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe

from . import forms
from . import models
from .forms import RegisterForm, WorkoutForm, ProfileForm

from django.views.generic import ListView, UpdateView

from .models import Workout, Profile

from _datetime import datetime, timedelta

import calendar
from .utils import Calendar



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


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = form.cleaned_data['group']
            group.user_set.add(user)
            models.Profile.objects.create(user=user,
                                          photo='unknown.jpg')
            return redirect('/')
    else:
        form = RegisterForm()
    return render(request, "registration/register.html", {'form': form})


@login_required
@permission_required('training.add_workout')
def create(request):
    error = ''
    if request.method == "POST":
        form = WorkoutForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            body = form.cleaned_data['workout_body']
            name = form.cleaned_data['user']
            start = form.cleaned_data['start_time']
            workout_ = Workout(title=title, workout_body=body, start_time=start)
            user_ = User.objects.get(username=name)
            user_.save()
            workout_.user = user_
            workout_.save()
            return redirect('/workouts')
        else:
            error = "Entered incorrect data"
    form = WorkoutForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'training/create.html', context)


@login_required
def update_profile(request):
    if request.method == "POST":
        form = forms.ProfileForm(data=request.POST,
                                 instance=request.user.profile,
                                 files=request.FILES)
        user_form = forms.UserForm(data=request.POST,
                                   instance=request.user)
        if form.is_valid():
            if not form.cleaned_data['photo']:
                form.cleaned_data['photo'] = request.user.profile.photo
                form.save()
            user_form.save()
            form.save()
            return render(request,
                          'training/index.html',
                          {'form': form,
                           'user_form': user_form})
    else:
        form = forms.ProfileForm(instance=request.user.profile)
        user_form = forms.UserForm(instance=request.user)
    return render(request, 'profile.html', {'form': form, 'user_form': user_form})


def view_profile(request, id):
    profile = get_object_or_404(models.Profile, pk=id)
    return render(request, 'training/view_profile.html', {'profile': profile})


def personal_workouts(request, id):
    pers_workouts = Workout.objects.filter(user_id=id)
    return render(request, 'training/personal_work.html', {'workouts': pers_workouts})


def all_clients(request):
    users_list = User.objects.all()
    return render(request, 'training/clients.html', {'users': users_list})


def workout_details(request, id):
    workout = get_object_or_404(models.Workout, pk=id)

    new_comment = None
    if request.method == 'POST':
        comment_form = forms.CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.workout = workout
            new_comment.save()
            return redirect(workout)
    else:
        comment_form = forms.CommentForm()

    return render(request,
                  'training/detail.html',
                  {'workout': workout,
                   'form': comment_form,
                   'was_added': new_comment})


def all_workouts(request):
    workouts_list = models.Workout.objects.all()
    return render(request,
                  'training/workouts.html',
                  {'workouts': workouts_list})


def update_workout(request, id):
    workout = get_object_or_404(models.Workout, pk=id)
    form = WorkoutForm(request.POST, instance=workout)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('/')
    form = WorkoutForm()
    context = {'form': form}
    return render(request, 'training/update.html', context)


def delete_workout(request, id):
    context = {}
    workout = get_object_or_404(models.Workout, pk=id)
    if request.method == 'POST':
        workout.delete()
        return redirect('/workouts')
    return render(request, 'training/delete.html', context)


class CalendarView(ListView):
    model = Workout
    template_name = 'training/calendar.html'
    success_url = reverse_lazy('calendar')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        d = get_date(self.request.GET.get('month', None))
        cal = Calendar(d.year, d.month)
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        return context


def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return datetime(year, month, day=1)
    return datetime.today()


def prev_month(d_obj):
    first = d_obj.replace(day=1)
    prev_month_ = first - timedelta(days=1)
    month = 'month=' + str(prev_month_.year) + '-' + str(prev_month_.month)
    return month


def next_month(d_obj):
    days_in_month = calendar.monthrange(d_obj.year, d_obj.month)[1]
    last = d_obj.replace(day=days_in_month)
    next_month_ = last + timedelta(days=1)
    month = 'month=' + str(next_month_.year) + '-' + str(next_month_.month)
    return month
