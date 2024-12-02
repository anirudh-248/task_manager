from django.shortcuts import render, redirect
from .models import Task

# Create your views here.
def index(request):
    has_tasks = Task.objects.filter(completed=False).exists()
    tasks = Task.objects.filter(completed=False)
    completed_tasks = Task.objects.filter(completed=True)
    return render(request, 'index.html', {'tasks': tasks, 'completed_tasks': completed_tasks, 'has_tasks': has_tasks})

def add_task(request):
    if request.method == 'POST':
        task = request.POST['task']
        Task.objects.create(task=task)
        return redirect('index')
    
def toggle_task_status(request):
    if request.method == 'POST':
        task_id = request.POST.get('task_id')
        task = Task.objects.get(id=task_id)
        task.completed = not task.completed
        task.save()
    return redirect('index')