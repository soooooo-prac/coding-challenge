from django.shortcuts import render
from .forms import TodoForm
from django.shortcuts import redirect

def home(request):
    return render(request, 'todo/home.html')

def add_todo(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = TodoForm()
    return render(request, 'todo/add.html', {'form': form})