from random import randint, choice

from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views import generic
from django.views.generic import View

from helper.models import Exercise, Category
from .forms import UserForm, SingleWorkoutForm, WorkoutForm, AddExerciseForm, DeleteExerciseForm, LoginForm


# Create your views here.

class UserFormView(View):
    form_class = UserForm
    template_name = 'helper/registration_form.html'

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            #cleaned (normalized) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            #returns User objects if credentials are correct
            user = authenticate(username=username, password=password)

            if user is not None:

                if user.is_active:
                    login(request, user)

                    return redirect('http://127.0.0.1:8000/login/helper/index.html/') #wpisać homepage
                
        return render(request, self.template_name, {'form': form})

class LoginView(View):
    form_class = LoginForm
    template_name = 'helper/login.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('http://127.0.0.1:8000/login/helper/index.html/')# Redirect to a success page.

        else:
            return HttpResponse('Nieprawidłowe dane')



class IndexView(View):
    def get(self, request):
        template_name = 'helper/index.html'
        return render(request, template_name)
    # def post(self, request):
    #     logout(request)
    #     return HttpResponse("udało się")

class CreateWorkout2(View):
    def get(self, request):
        form = WorkoutForm
        template_name = 'helper/create_workout1.html'
        return render(request, template_name, {"form": form})
    def post(self, request):
        form = WorkoutForm(request.POST)
        if form.is_valid():
            level = form.cleaned_data['level']
            period = int(form.cleaned_data['period'])
            weekly_quantity = int(form.cleaned_data['weekly_quantity'])
            #all_exercises=list(Exercise.objects.filter(level=level))

            arms_exercises=list(Exercise.objects.filter(category=1, level=level))
            legs_exercises = list(Exercise.objects.filter(category=2, level=level))
            core_exercises = list(Exercise.objects.filter(category=3, level=level))

            exercises = []
            if period == 2:
                for j in range(4):

                    for i in range(weekly_quantity):
                        if i == 0:
                            for x in range(6):
                                exercises.append(choice(arms_exercises))
                            exercises.append('\n')
                        if i == 1:
                            for x in range(6):
                                exercises.append(choice(legs_exercises))
                            exercises.append('\n')
                        if i == 2:
                            for x in range(6):
                                exercises.append(choice(core_exercises))
                            exercises.append('\n')
                        if i == 3:
                            for x in range(6):
                                exercises.append(choice(arms_exercises))
                            exercises.append('\n')
                        if i == 4:
                            for x in range(6):
                                exercises.append(choice(legs_exercises))
                            exercises.append('\n')
            else:
                for i in range(weekly_quantity):
                    if i == 0:
                        for x in range(6):
                            exercises.append(choice(arms_exercises))
                        exercises.append('\n')
                    if i == 1:
                        for x in range(6):
                            exercises.append(choice(legs_exercises))
                        exercises.append('\n')
                    if i == 2:
                        for x in range(6):
                            exercises.append(choice(core_exercises))
                        exercises.append('\n')
                    if i == 3:
                        for x in range(6):
                            exercises.append(choice(arms_exercises))
                        exercises.append('\n')
                    if i == 4:
                        for x in range(6):
                            exercises.append(choice(legs_exercises))
                        exercises.append('\n')
                    # for i in range(6):
                    #     exercises.append(choice(all_exercises))
                    # exercises.append('--------------')


            return render(request, 'helper/single_workout.html', {'exercises': exercises})
        else:
            return render(request, 'helper/create_workout1.html',
                                  {"form": form,
                                   })

class CreateWorkout1(View):
    def get(self, request):
        form = SingleWorkoutForm
        template_name = 'helper/create_workout1.html'
        return render(request, template_name, {"form": form})
    def post(self, request):
        form = SingleWorkoutForm(request.POST)
        if form.is_valid():
            level = form.cleaned_data['poziom']
            category = form.cleaned_data['kategoria']
            quantity_of_exercises = form.cleaned_data['ilość_ćwiczeń']
            bar = form.cleaned_data['drążek']
            parallel_bars = form.cleaned_data['poręcze']


            all_exercises=list(Exercise.objects.filter(level=level,
                                           category=category,
                                            parallel_bars=parallel_bars,
                                                      bar=bar ))
            exercises = []
            for i in range(int(quantity_of_exercises)):
                exercises.append(choice(all_exercises))

            return render(request, 'helper/single_workout.html', { 'exercises': exercises })
        else:
            return render(request, 'helper/create_workout1.html',
                            {"form": form,
                             })

class OneDayWorkout(View): #nieużywane
    def get(self, request):
        template_name = 'helper/single_workout.html'
        exercises_random = []

        for x in range(2):
            category = Category.objects.get(name='Ręce')
            exercises_all = Exercise.objects.filter(category=category).all()
            exercises_random.append(choice(exercises_all))

        ctx = {
            'exercises': exercises_random
        }
        return render(request, template_name, ctx)

class ShowExercises(View):
    def get(self, request):
        template_name = 'helper/exercises.html'
        exercises = Exercise.objects.all()
        ctx = {
            'exercises': exercises
        }
        return render(request, template_name, ctx)

class Description(View):
    def get(self, request, id):
        template_name = 'helper/description.html'
        exercise = Exercise.objects.get(id=id)
        ctx = {
            'exercise': exercise
        }
        return render(request, template_name, ctx)


class AddExercise(PermissionRequiredMixin, View):
    permission_required = 'add_exercise'
    def get(self, request):
        form = AddExerciseForm
        template_name = 'helper/add_exercise.html'
        return render(request, template_name, {"form": form})
    def post(self, request):
        form = AddExerciseForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            reps = form.cleaned_data['reps']
            level = form.cleaned_data['level']
            category = form.cleaned_data['category']
            bar = form.cleaned_data['bar']
            parallel_bars = form.cleaned_data['parallel_bars']
            Exercise.objects.create(name=name,
                                    description=description,
                                    reps=reps,
                                    level=level,
                                    category=category,
                                    bar=bar,
                                    parallel_bars = parallel_bars)

            return redirect('exercises.html')
        else:
            return HttpResponse("Wystąpił błąd w przesyłaniu formularza")

class DeleteExercise(PermissionRequiredMixin, View):
    permission_required = 'delete_exercise'
    def get(self, request):
        form = DeleteExerciseForm
        template_name = 'helper/delete_exercise.html'
        return render(request, template_name, {"form": form})
    def post(self, request):
        form = DeleteExerciseForm(request.POST)
        if form.is_valid():
            id = form.cleaned_data['id']
            x = Exercise.objects.get(id=id)
            x.delete()
            return redirect('exercises.html')
        else:
            return HttpResponse("Wystąpił błąd w przesyłaniu formularza")
