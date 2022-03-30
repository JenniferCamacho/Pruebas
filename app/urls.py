from django.urls import path 
from . import views 

app_name = 'app' 
urlpatterns = [
    path('hola/', views.hola, name='hola'), 
    # path('Ejm.CATEGORIAS/', views.index, name='index'), PARA guiar a que dirección dirigirse 
    path('categorias/', views.categorias, name='categorias'), 
    path('peliculas/', views.peliculas, name='peliculas'), 
]