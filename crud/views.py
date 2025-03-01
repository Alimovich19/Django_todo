from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm

# Create your views here.
def AllTasksView(request):
    tasks = Todo.objects.all()
    form = TodoForm()
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_tasks')
    return render(request, 'all_tasks.html', {'tasks': tasks, 'form': form})

def DeleteTask(request, pk):
    task = Todo.objects.get(id = pk)
    task.delete()
    return redirect('all_tasks')

def UpdateTask(request, pk):
    todo = Todo.objects.get(id=pk)
    updateForm = TodoForm(instance = todo)
    if request.method == 'POST':
        updateForm = TodoForm(request.POST, instance = todo)
        if updateForm.is_valid():
            updateForm.save()
            return redirect('all_tasks')
    return render(request, 'update_task.html', {'todo':todo, 'updateform': updateForm})
