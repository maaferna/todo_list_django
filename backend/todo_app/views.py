from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.template.loader import render_to_string
from django.urls import reverse

from .models import Task
from .forms import TaskForm

def home(request):
    tasks = Task.objects.filter(user=request.user).order_by('-modified_at')
    form = TaskForm(request.POST or None, initial={'tasks': tasks})
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user  # Assign the current user to the task
            task.save()
            tasks = Task.objects.filter(user=request.user).order_by('-modified_at')
            html = render_to_string('partials/_task_list.html', {'tasks': tasks})
            message = "Task successfully saved!"  # Add your desired success message
            return JsonResponse({'html': html, 'message': message})
    else:
        form = TaskForm()
    return render(request, 'todo/home.html', {'form': form, 'tasks': tasks})

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    title = task.title  # Get the title before deletion
    task.delete()
    tasks = Task.objects.filter(user=request.user).order_by('-modified_at')
    html = render_to_string('partials/_task_list.html', {'tasks': tasks})
    return JsonResponse({'html': html, 'title': title})


def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    title = task.title  # Get the title before edition

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            # Return a success message or an updated task list
            tasks = Task.objects.filter(user=request.user).order_by('-modified_at')
            html = render_to_string('partials/_task_list.html', {'tasks': tasks})
            home_url = reverse('home')  # Assuming 'home' is the name of your home URL pattern
            print("Console log the home: ", home_url)
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                # If the request is an AJAX request, return a JSON response
                return JsonResponse({'html': html, 'title': title, 'home_url': home_url})
            else:
                # If the request is not an AJAX request, redirect to the home URL
                return redirect(home_url)
