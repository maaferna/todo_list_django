from django.http import JsonResponse
from django.shortcuts import render
from django.template.loader import render_to_string

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
            return JsonResponse({'html': html})
    else:
        form = TaskForm()
    return render(request, 'todo/home.html', {'form': form, 'tasks': tasks})


