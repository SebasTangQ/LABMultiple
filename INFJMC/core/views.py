from contextlib import nullcontext
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    titulo = "<h1>Informatica USM</h1> <hr> <a href='http://127.0.0.1:8000/carreras/'>Carreras</a> <a href='http://127.0.0.1:8000/docentes/'>Docentes</a> <hr>"
    return HttpResponse(titulo)

def carreras(request):
    titulo = "<h1>Carreras</h1> <hr> <a href='http://127.0.0.1:8000/'>Home</a> <a href='http://127.0.0.1:8000/docentes/'>Docentes</a>"
    return HttpResponse(titulo)

def docentes(request):
    titulo = "<h1>Docentes</h1><hr> <a href='http://127.0.0.1:8000/'>Home</a> <a href='http://127.0.0.1:8000/carreras/'>Carreras</a>"
    return HttpResponse(titulo)