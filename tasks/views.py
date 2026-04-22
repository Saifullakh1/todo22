from django.shortcuts import render, redirect
from .models import Task


def list(request):
    if request.user.is_superuser:
        tasks = Task.objects.all()
    else:
        tasks = Task.objects.filter(user=request.user.id)
    return render(request, './index.html', {'tasks': tasks})


def create(request):
    if request.method == 'POST':
        user = request.user
        title = request.POST.get('title')
        description = request.POST.get('description')
        deadline = request.POST.get('deadline')
        Task.objects.create(title=title, description=description, user=user, deadline=deadline)
        return redirect('list')
    return render(request, 'create.html')


def detail(request, id):
    task = Task.objects.get(id=id)
    return render(request, './detail.html', {'task': task})


def update(request, id):
    task = Task.objects.get(id=id)
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        deadline = request.POST.get('deadline')
        is_finished = 'is_finished' in request.POST
        task.title = title
        task.description = description
        task.deadline = deadline
        task.is_finished = is_finished
        task.save()
        return redirect('detail', task.id)
    else:
        return render(request, 'update.html', context={"task": task})


def delete(request, id):
    if request.method == 'POST':
        task = Task.objects.get(id=id)
        task.delete()
        return redirect('list')
    return render(request, 'detail.html')