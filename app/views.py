from http.client import HTTPResponse
from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from app.models import Categoria

# Create your views here.

def peliculas(request):
    return HttpResponse ('Peliculas')

def inicio(request):
    return render (request,'app/inicio.html')

def categorias(request):

    lista_categorias=Categoria.objects.all()

    contexto={
        'titulo':'Blockbuster',
        'categorias':[
        {'id':1, 'nombre': 'terror'},
        {'id':2, 'nombre': 'romance'},
        {'id':3, 'nombre': 'aventuras'},
        {'id':4, 'nombre': 'Comedia'},

        ]
    }
    
    return render(request, 'app/base.html',contexto)

def categoria(request, id):
    return HttpResponse (f'Esta es una Categoria {id}')