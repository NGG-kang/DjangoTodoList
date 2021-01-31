
from django.urls import path
from . import views

app_name='toDo'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('toDo', views.IndexView.as_view(), name='index'),
    path('write', views.writeView.as_view(), name='write'),
    path('writetoDo', views.writetoDo, name='writetoDo'),
    path('<int:pk>', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/modify', views.ModifyView.as_view(), name='modify'),
    path('<int:pk>/modify/modifytoDo', views.modifytoDo, name='modifytoDo'),
    path('<int:pk>/delete', views.deltoDo, name='delete'),
]