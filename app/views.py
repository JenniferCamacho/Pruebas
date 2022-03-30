from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def peliculas(request):
    return HttpResponse ('Peliculas')

def categorias(request):
    return HttpResponse ('Categorias')

def categoria(request, id):
    return HttpResponse (f'Esta es una Categoria {id}')