from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.http import HttpResponse

from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required, permission_required

from . import forms
from . import models
from .forms import RegisterForm, WorkoutForm

from django.views.generic import ListView, UpdateView

from .models import Workout



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
            workout_ = Workout(title=title, workout_body=body)
            # workout_.save()
            user_ = User.objects.get(username=name)
            user_.save()
            workout_.user = user_
            workout_.save()
            # request.user.user_workout.add(t)
            return redirect('/workouts')
        else:
            error = "Entered incorrect data"
    form = WorkoutForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'training/create.html', context)


# class MaterialListView(LoginRequiredMixin, ListView):
#     queryset = models.Workout.objects.all()
#     context_object_name = 'workouts'
#     template_name = 'training/workouts.html'


@login_required
def view_profile(request):
    return render(request, 'profile.html', {'user': request.user})


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

#
# class ProfileView(UpdateView):
#     model = User
#
#     def get_initial(self):
#         initial = super(ProfileView, self).get_initial()
#         try:
#             current_group = self.object.groups.get()
#         except:
#             # exception can occur if the edited user has no groups
#             # or has more than one group
#             pass
#         else:
#             initial['group'] = current_group.pk
#         return initial
#
#     def get_form_class(self):
#         return ProfileForm
#
#     def form_valid(self, form):
#         self.object.groups.clear()
#         self.object.groups.add(form.cleaned_data['group'])
#         return super(ProfileView, self).form_valid(form)
