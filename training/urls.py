from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

from django.conf import settings
from django.conf.urls.static import static


class MyHack(auth_views.PasswordResetView):
    success_url = reverse_lazy('training:password_reset_done')


urlpatterns = [
    path('', views.index, name="home"),
    path('workouts/', views.all_workouts, name='workouts'),
    path('about_me/', views.about_me, name='about_me'),
    path('detail/<int:id>/', views.workout_details, name='workout_details'),
    path('update/<int:id>/', views.update_workout, name='update_workout'),
    path('delete/<int:id>', views.delete_workout, name='delete_workout'),
    path('create/', views.create, name='create'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('password_reset/', MyHack.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             success_url=reverse_lazy('training:password_reset_compete')
         ), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('register/', views.register, name="register"),
    path('profile/', views.view_profile, name='profile'),
    ]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
