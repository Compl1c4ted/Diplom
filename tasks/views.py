from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.template.loader import render_to_string
from .models import Tasks
from .forms import TaskForm


def view_tasks(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/tasks/tasks_list')
    else:
        form = TaskForm()
    tasks = Tasks.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks, 'form': form})


def task_detail(request, id):
    task = get_object_or_404(Tasks, id=id)
    # Возвращаем данные задачи в формате JSON
    data = {
        'title': task.title,
        'descriptions': task.descriptions,
        'status': task.get_status_display(),
    }
    return JsonResponse(data)


def delete_task(request, id):
    print(f"Получил запрос на удаление: {id}")
    task = get_object_or_404(Tasks, id=id)
    if request.method == 'POST':
        task.delete()
        return redirect('/tasks/tasks_list')


def edit_task(request, id):
    task = get_object_or_404(Tasks, id=id)
    if request.method == 'POST':
        form = TaskForm(request.POST, id)
        if form.is_valid():
            form.save()
            return redirect('/tasks/tasks_list')
