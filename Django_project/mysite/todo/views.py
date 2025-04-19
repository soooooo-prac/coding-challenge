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