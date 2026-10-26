from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('categorias/', views.listar_categorias, name='listar_categorias'),
    path('categorias/nova/', views.cadastrar_categoria, name='cadastrar_categoria'),
    path('categorias/editar/<int:pk>/', views.atualizar_categoria, name='atualizar_categoria'),
]