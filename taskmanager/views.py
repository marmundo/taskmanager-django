from datetime import datetime
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .models import Task
# Create your views here.
def index(request):
    try:
        latest_task_list = Task.objects.order_by('-created_at')[:5]
    except Task.DoesNotExist:
        raise Http404("Nenhuma Tarefa Cadastrada")
    context = {'latest_task_list': latest_task_list}
    return render(request, 'taskmanager/index.html', context)

def detail(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    return render(request, 'taskmanager/detail.html', {'task': task})   

def edit(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    print(task)
    return render(request, 'taskmanager/edit.html', {'task': task})

def create(request):
    print(request.method)
    if(request.method == 'POST'):
        title = request.POST['title']
        description = request.POST['description']
        completed = request.POST.get('completed', False)=='on'
        task = Task(title=title, description=description, completed=completed)
        task.save()
        return HttpResponseRedirect(reverse('taskmanager:index'))
    return render(request, 'taskmanager/create.html')

def update(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.title=request.POST['title']
    task.description=request.POST['description']
    task.updated_at=datetime.now()
    task.completed=request.POST.get('completed', False)=='on'
    print(request.POST.get('completed', False)=='on')
    task.save()
    return HttpResponseRedirect(reverse('taskmanager:index'))

def delete(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.delete()
    return HttpResponseRedirect(reverse('taskmanager:index'))