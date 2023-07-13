from django.shortcuts import render, redirect
from .models import Todo
from django.contrib import messages
from .forms import TodoCreateForm

def home(request):
    all = Todo.objects.all()
    return render(request, 'home.html', {'todos': all})


def father(request):
    return render(request, 'name.html')


def say_hello(request):
    person = {'name': 'ali'}
    return render(request, 'hello.html', context=person)


def detail(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    return render(request, 'detail.html', {'todo': todo})

def delete(request, todo_id):
    Todo.objects.get(id=todo_id).delete()
    messages.success(request, 'Success!',extra_tags='success')
    return redirect('home')
def create(request):
   if request.method == 'POST':
       form = TodoCreateForm(request.POST)
       if form.is_valid():
           cd = form.cleaned_data
           Todo.objects.create(title=cd['title'],body=cd['body'],created = cd['created'])
           messages.success(request, 'database created')
           return redirect('create')
   else:
        form = TodoCreateForm()
        return render(request, 'create.html', {'form': form})
