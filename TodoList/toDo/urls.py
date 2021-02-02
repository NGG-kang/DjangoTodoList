
from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

app_name = 'toDo'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('toDo', views.IndexView.as_view(), name='index'),
    path('write', login_required(views.writeView.as_view()), name='write'),
    path('writetoDo', views.writetoDo, name='writetoDo'),
    path('<int:pk>', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/modify', views.ModifyView.as_view(), name='modify'),
    path('<int:pk>/modify/modifytoDo', views.modifytoDo, name='modifytoDo'),
    path('<int:pk>/delete', views.deltoDo, name='delete'),
    
    path('loginview', views.LoginView.as_view(), name='loginview'),
    path('signview', views.SignView.as_view(), name='signview'),
    
    path('logoutok', views.logoutok, name='logoutok'),
    path('loginview/loginok', views.loginok, name='loginok'),
    path('signview/signok', views.signok, name='signok'),
    
]