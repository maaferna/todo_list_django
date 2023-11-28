# todo_app/views.py

from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

def home(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to the home page after adding a task
    else:
        form = TaskForm()

    return render(request, 'todo/home.html', {'form': form})

