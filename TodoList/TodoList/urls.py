from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('toDo/', include('toDo.urls')),
    path('api/', include('restframwork.urls')),
]
