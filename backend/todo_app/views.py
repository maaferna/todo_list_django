from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.template.loader import render_to_string
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout


from .models import Task
from .forms import *

@login_required()  # Redirect to your custom login URL
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
            messages.error(request,error_message)  # Add success message to Django messages
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


def view_login(request):
  if request.method == "POST":
    form = AuthenticationForm(request, data=request.POST)
    if form.is_valid():
      username = form.cleaned_data.get('username')
      password = form.cleaned_data.get('password')
      user = authenticate(username=username,
      password=password)
      if user is not None:
        login(request, user)
        messages.info(request, f"Iniciaste sesión como: {username}.")
        return HttpResponseRedirect('/')
      else:
        messages.error(request,"Invalido username o password.")
    else:
      messages.error(request,"Invalido username o password.")
  form = AuthenticationForm()
  return render(request=request, template_name="registration/login.html",context={"login_form":form})


def view_register(request):
  if request.method == "POST":
    form = RegistroUsuarioForm(request.POST)
    if form.is_valid():
      user = form.save()
      #user.groups.add(Group.objects.get(name="visualizar_catalogo"))
      login(request, user)
      messages.success(request, "Registrado Satisfactoriamente." )
      return HttpResponseRedirect('/')
    messages.error(request, "Registro invalido. Algunos datos ingresados no son correctos")
  form = RegistroUsuarioForm()
  return render (request=request, template_name="registration/register.html", context={"register_form":form})


@login_required
def view_logout(request):
  logout(request)
  messages.info(request, "Se ha cerrado la sesión satisfactoriamente.")
  return redirect('home')


def custom_permission_denied(request, exception):
    return render(request, 'registration/custom_permission_denied.html', status=403)


@login_required()  # Redirect to your custom login URL
def dashboard(request):
    high_priority_tasks = Task.objects.filter(user=request.user, priority='high')
    medium_priority_tasks = Task.objects.filter(user=request.user, priority='medium')
    low_priority_tasks = Task.objects.filter(user=request.user, priority='low')
    important_priority_tasks = Task.objects.filter(user=request.user, priority='important')
    print(high_priority_tasks)
    return render(
        request,
        'todo/dashboard.html',
        {
            'important_priority_tasks': important_priority_tasks,
            'high_priority_tasks': high_priority_tasks,
            'medium_priority_tasks': medium_priority_tasks,
            'low_priority_tasks': low_priority_tasks,
        }
    )


def get_task_details(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    # Customize the data you want to include in the JSON response
    task_details = {
        'title': task.title,
        'description': task.description,
        'effort': task.effort,
        'created_at': task.created_at,
        'modified_at': task.modified_at
    }

    return JsonResponse({'details': task_details})