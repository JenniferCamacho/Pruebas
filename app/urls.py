from django.urls import path 
from . import views 

app_name = 'app' 
urlpatterns = [
    path('inicio/', views.inicio, name='inicio'), 
    path('categorias/', views.categorias, name='categorias'), 
    path('categorias/<int:id>/', views.categoria, name='categoria'), 
    path('peliculas/', views.peliculas, name='peliculas'), 
]