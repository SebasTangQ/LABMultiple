from contextlib import nullcontext
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

menu = "<hr><ul>"
menu +=" <li><a href='http://127.0.0.1:8000/'>Inicio</a></li>"
menu +=" <li><a href='http://127.0.0.1:8000/carreras/'>Carreras</a></li>"
menu +=" <li><a href='http://127.0.0.1:8000/docentes/'>Docentes</a></li>"
menu +="</ul>"

contenido = "<hr><p> lorem. </p>"
# Create your views here.
def home(request):
    titulo = "<h1>Informatica USM</h1>"
    html = titulo+menu+contenido
    return HttpResponse(html)

def carreras(request):
    titulo = "<h1>Carreras</h1>"
    html = titulo+menu
    return HttpResponse(html)

def docentes(request):
    titulo = "<h1>Docentes</h1>"
    html = titulo+menu
    return HttpResponse(html)