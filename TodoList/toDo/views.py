from django.shortcuts import render
from django.views import generic
from .models import TodoList
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, HttpRequest
# Create your views here.


class IndexView(generic.ListView):
    template_name = 'toDo/index.html'
    context_object_name = 'todolist'
    
    def get_queryset(self):
        return TodoList.objects.all()


class writeView(generic.TemplateView):
    template_name = 'toDo/write.html'


class DetailView(generic.TemplateView):
    model = TodoList
    template_name = 'toDo/detail.html'
    


class ModifyView(generic.DetailView):
    template_name = 'toDo/modify.html'
    model = TodoList
    

def writetoDo(request):
    if(request.method=="POST"):
        todo = request.POST.get('todo')
        todolist = TodoList()
        todolist.toDo = todo
        todolist.pub_date = timezone.now()
        todolist.author = request.user
        todolist.save()
    return HttpResponseRedirect('/toDo')