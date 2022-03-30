from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hola(request):
    return HttpResponse ('hola')

def peliculas(request):
    return HttpResponse ('Peliculas')

def categorias(request):
    return HttpResponse ('Categorias')