from django.shortcuts import render,get_object_or_404
from django.views import generic
from .models import TodoList
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, HttpRequest
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.


class IndexView(generic.ListView):
    template_name = 'toDo/index.html'
    context_object_name = 'todolist'
    paginate_by = 5
    
    def get_queryset(self):
        return TodoList.objects.all()


class writeView(generic.TemplateView):
    template_name = 'toDo/write.html'


class DetailView(generic.DetailView):
    template_name = 'toDo/detail.html'
    model = TodoList
    context_object_name = 'todo'

class ModifyView(generic.DetailView):
    template_name = 'toDo/modify.html'
    model = TodoList
    context_object_name = 'todo'
    

class LoginView(generic.TemplateView):
    template_name = 'toDo/loginview.html'


class SignView(generic.TemplateView):
    template_name = 'toDo/signview.html'    

@login_required()
def writetoDo(request):
    if(request.method=="POST"):
        todo = request.POST.get('todo')
        todolist = TodoList()
        todolist.toDo = todo
        todolist.pub_date = timezone.now()
        todolist.author = request.user
        todolist.save()
    return HttpResponseRedirect('/toDo')

@login_required()
def modifytoDo(request, pk):
    todo = get_object_or_404(TodoList, pk=pk)
    if(request.user != todo.author):
        return redirect('toDo:index')
    if(request.method=="POST"):
        todo.toDo = request.POST.get('toDo')
        todo.pub_date = timezone.now()
        todo.save()
    return redirect('toDo:detail', pk=todo.id)

@login_required()
def deltoDo(request, pk):
    todo = get_object_or_404(TodoList, pk=pk)
    todo.delete()
    return HttpResponseRedirect('/toDo')


def loginok(reuqest):
    username = reuqest.POST['username']
    password = reuqest.POST['password']
    user = authenticate(reuqest, username=username, password=password)
    if user is not None:
        login(reuqest, user)
    return HttpResponseRedirect('/toDo')

def logoutok(reuqest):
    logout(reuqest)
    return HttpResponseRedirect('/toDo')

def signok(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    email = request.POST.get('email')
    cuser = User.objects.create_user(username,email,password)
    cuser.save()

    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
    return HttpResponseRedirect('/toDo')