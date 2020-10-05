from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.

def hello(request):
    return HttpResponse('Bem vindo ao Sistema de Recursos Humanos!!')
    

def cadastro(request):
    return render(request, 'rh/index.html')


