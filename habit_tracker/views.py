from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .models import Signup
from .forms import SignupForm
from datetime import datetime


def home_view(request):
    return render(request, 'habit_tracker/home.html')



def habit_tracker(request):
    # Example of possible habits data
    habits = [
        {'name': 'Exercise', 'completed': True, 'created_at': '2023-05-01'},
        {'name': 'Read Book', 'completed': False, 'created_at': '2023-04-15'},
        {'name': 'Meditate', 'completed': True, 'created_at': '2023-03-20'},
    ]

    context = {
        'habits': habits,
    }
    return render(request, 'habit_tracker/habit_tracker.html', context)

def signup_success(request):
    return render(request, 'habit_tracker/signup_success.html')


def signup(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        occupation = request.POST['occupation']

        signup = Signup(name=name, email=email, password=password, occupation=occupation)
        signup.save()

        return redirect('signup_success')  

    return render(request, 'signup.html')

