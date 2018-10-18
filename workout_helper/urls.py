"""workout_helper URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url

from helper import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^register/$', views.UserFormView.as_view(), name='register'),
    url(r'^login/$', views.LoginView.as_view(), name='login'),
    url(r'^login/helper/index.html/$', views.IndexView.as_view(), name='index'),
    #url(r'^login/helper/index.html/create_workout2.html$', views.CreateWorkout2.as_view(), name='create_workout2'),
    url(r'^login/helper/index.html/create_workout1.html$', views.CreateWorkout1.as_view(), name='create_workout1'),
    #url(r'^login/helper/index.html/single_workout.html$', views.OneDayWorkout.as_view(), name='single_workout'),
    url(r'^login/helper/index.html/exercises.html$', views.ShowExercises.as_view(), name='show_exercises'),
    url(r'^login/helper/index.html/helper/description.html/(?P<id>(\d)+)', views.Description.as_view(), name='description'),
    url(r'^login/helper/index.html/add_exercise.html', views.AddExercise.as_view(), name='add_exercise'),
    url(r'^login/helper/index.html/delete_exercise.html', views.DeleteExercise.as_view(), name='delete_exercise')
    ]

