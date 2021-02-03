from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet


class test(ModelViewSet):
    def dispatch(self, request, *args, **kwargs):