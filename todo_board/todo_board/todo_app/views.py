from django.shortcuts import render, HttpResponse, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import List, Task
from django.urls import reverse_lazy

# Create your views here.


def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if pass1 != pass2:
            return HttpResponse("password and confirm password didn't match")
        else:
            my_user = User.objects.create_user(uname, email, pass1)
            my_user.save()
            return redirect('login')

        print(uname, email, pass1, pass2)

    return render(request, 'registration.html')

def loginpage(request):
    
    if request.method == 'POST':
        usname = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user = authenticate(request, username=usname, password=pass1)
        if user is not None:
            login(request, user)
            return redirect('tasklistview')
        else:
            return HttpResponse("username or password are incorrect")

    return render(request, 'login.html')


def logoutpage(request):
    logout(request)
    return redirect('login')

#@login_required(login_url='login')   # login_url='login' keeps the login page if we http://127.0.0.1:8000/home/ if we dont put this it will throw 404
class TaskListView(ListView):
    context_object_name = 'lists'
    model = List
    template_name = 'tasklistview.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        lists = List.objects.filter(user=self.request.user)  # Retrieve all lists

        lists_and_tasks = []
        for list_item in lists:
            tasks = Task.objects.filter(list=list_item) # retrive all tasks in their lists
            lists_and_tasks.append((list_item, tasks))

        context['lists_and_tasks'] = lists_and_tasks
        # context['lists_and_tasks'] = context['lists_and_tasks'].filter(user=self.request.user)
        return context
        
class TaskDetail(DetailView):
    context_object_name = 'task'
    model = Task
    template_name = 'taskdetail.html'

class ListCreate(CreateView):
    model = List
    fields = ['title']
    template_name = 'list_form.html'
    success_url = reverse_lazy('tasklistview') # sends back to lists page after creating the task

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ListCreate, self).form_valid(form)

class TaskCreate(CreateView):
    model = Task
    fields = ['list', 'title', 'description', 'completed']
    template_name = 'task_form.html'
    success_url = reverse_lazy('tasklistview') # sends back to lists page after creating the task

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)
    

class TaskUpdate(UpdateView):
    model = Task
    fields = ['title', 'description', 'completed']
    template_name = 'task_form.html'
    success_url = reverse_lazy('tasklistview')

class TaskDelete(DeleteView):
    model = Task
    context_object_name = 'task'
    template_name = 'task_confirm_delete.html'
    success_url = reverse_lazy('tasklistview')
