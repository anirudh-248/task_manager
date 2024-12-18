from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Task

# Create your views here.

def index(request):
    return render(request, 'index.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('manager')
        else:
            messages.info(request, 'Invalid email or password')
            return redirect('login')
    return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password != password2:
            messages.info(request, 'Passwords do not match')
            return redirect('register')
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            if user:
                messages.success(request, 'Account created successfully')
                return redirect('login')
            else:
                messages.info(request, 'An error occurred while creating your account')
                return redirect('register')
    return render(request, 'register.html')

def manager(request):
    if request.user.is_authenticated:
        has_tasks = Task.objects.filter(user=request.user, completed=False).exists()
    else:
        has_tasks = False
    tasks = Task.objects.filter(user=request.user, completed=False)
    completed_tasks = Task.objects.filter(user=request.user, completed=True)
    return render(request, 'manager.html', {'tasks': tasks, 'completed_tasks': completed_tasks, 'has_tasks': has_tasks})

def add_task(request):
    if request.method == 'POST':
        task = request.POST['task']
        user = request.user
        Task.objects.create(task=task, user=user)
        return redirect('manager')
    
def toggle_task_status(request):
    if request.method == 'POST':
        task_id = request.POST.get('task_id')
        task = Task.objects.get(id=task_id)
        task.completed = not task.completed
        task.save()
    return redirect('manager')