from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.template.loader import render_to_string
from django.urls import reverse
from django.contrib import messages

from .models import Task
from .forms import TaskForm

def home(request):
    tasks = Task.objects.filter(user=request.user).order_by('-modified_at')

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()

            tasks = Task.objects.filter(user=request.user).order_by('-modified_at')
            html = render_to_string('partials/_task_list.html', {'tasks': tasks})

            # Modify the home_url to redirect to the homepage after adding a new task
            home_url = reverse('home')

            title = task.title
            message = "Task successfully saved!: " + title 
            
            messages.success(request, message)  # Add success message to Django messages

            return JsonResponse({'html': html, 'home_url': home_url, 'title': title})
        else:
            error_message = "Please select values for both priority and effort."
            return JsonResponse({'error_message': error_message})

    form = TaskForm()
    return render(request, 'todo/home.html', {'form': form, 'tasks': tasks})

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    title = task.title  # Get the title before deletion
    task.delete()
    tasks = Task.objects.filter(user=request.user).order_by('-modified_at')
    html = render_to_string('partials/_task_list.html', {'tasks': tasks})
    home_url = reverse('home')  # Assuming 'home' is the name of your home URL pattern
    message = "Task successfully deleted!: " + title 
    messages.warning(request, message)  # Add success message to Django messages
    return JsonResponse({'html': html, 'title': title, 'home_url': home_url})


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
            title = task.title
            message = "Task successfully updated!: " + title 
            
            messages.info(request, message)  # Add success message to Django messages
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                # If the request is an AJAX request, return a JSON response
                return JsonResponse({'html': html, 'title': title, 'home_url': home_url})
            else:
                # If the request is not an AJAX request, redirect to the home URL
                return redirect(home_url)
