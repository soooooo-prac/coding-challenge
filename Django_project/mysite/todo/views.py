from django.shortcuts import render
from .forms import TodoForm
from django.shortcuts import redirect
from .models import Todo

def home(request):
    todos = Todo.objects.all().order_by('-created_at')
    return render(request, 'todo/home.html', {'todos': todos})

def add_todo(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = TodoForm()
    return render(request, 'todo/add.html', {'form': form})

def delete_todo(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.delete()
    return redirect('/')

def toggle_todo(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.is_done = not todo.is_done
    todo.save()
    return redirect('/')

def edit_todo(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = TodoForm(instance=todo)
    return render(request, 'todo/edit.html', {'form': form})
