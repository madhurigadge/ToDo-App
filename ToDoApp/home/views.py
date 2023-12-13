from django.shortcuts import render,HttpResponse,redirect
from . models import Task
from .forms import TaskForm, UpdateForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required




@login_required(login_url='/loginn')
def home(request):
    if request.method=='POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home:home')

    tasks= Task.objects.all()
    form = TaskForm()
    print(form)
    return render(request, 'home.html', {'tasks': tasks, 'form': form})

def edit(request, id=id):
    task = Task.objects.get(id=id)
    if request.method == 'POST':
        form = UpdateForm(request.POST or None, instance=task)
        if form.is_valid():
            form.save()
            return redirect('home:home')

    form = UpdateForm(request.POST or None, instance=task)
    print(form)
    return render(request, 'edit.html', {'form': form})

def completed(request, id):
    task = Task.objects.get(id=id)
    if task.completed != True:
        task.completed=True
        task.save()
        return redirect('home:home')


def delete(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    return redirect('home:home')

def priority(request, choice):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home:home')

    tasks = Task.objects.filter(priority=choice)
    form = TaskForm()
    print(form)
    return render(request, 'home.html', {'tasks': tasks, 'form': form})


def status(request, choice):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home:home')

    tasks = Task.objects.filter(completed=choice)
    form = TaskForm()
    print(form)
    return render(request, 'home.html', {'tasks': tasks, 'form': form})


def signup(request):
    if request.method == 'POST':
        fnm=request.POST.get('fnm')
        emailid=request.POST.get('emailid')
        pwd=request.POST.get('pwd')
        print(fnm,emailid,pwd)
        my_user=User.objects.create_user(fnm,emailid,pwd)
        my_user.save()
        return redirect('/loginn/home/')
    
    return render(request, 'signup.html')
        
     
def loginn(request):
    if request.method == 'POST':
        fnm=request.POST.get('fnm')
        pwd=request.POST.get('pwd')
        print(fnm,pwd)
        userr=authenticate(request,username=fnm,password=pwd)
        if userr is not None:
            login(request,userr)
            return redirect('/home/')
        else:
            return HttpResponse("Username or password is incorrect!!")
               
    return render(request, 'login.html')

def logout(request):
    return redirect('/loginn')