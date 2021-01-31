from django.shortcuts import render,get_object_or_404
from django.views import generic
from .models import TodoList
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, HttpRequest
from django.shortcuts import redirect
# Create your views here.


class IndexView(generic.ListView):
    template_name = 'toDo/index.html'
    context_object_name = 'todolist'
    
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

def writetoDo(request):
    if(request.method=="POST"):
        todo = request.POST.get('todo')
        todolist = TodoList()
        todolist.toDo = todo
        todolist.pub_date = timezone.now()
        todolist.author = request.user
        todolist.save()
    return HttpResponseRedirect('/toDo')

def modifytoDo(request, pk):
    todo = get_object_or_404(TodoList, pk=pk)
    if(request.method=="POST"):
        todo.toDo = request.POST.get('toDo')
        todo.pub_date = timezone.now()
        todo.save()
    return redirect('toDo:detail', pk=todo.id)

def deltoDo(request, pk):
    todo = get_object_or_404(TodoList, pk=pk)
    todo.delete()
    return HttpResponseRedirect('/toDo')