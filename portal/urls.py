from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('categorias/', views.listar_categorias, name='listar_categorias'),
    path('categorias/nova/', views.cadastrar_categoria, name='cadastrar_categoria'),
    path('categorias/editar/<int:pk>/', views.atualizar_categoria, name='atualizar_categoria'),
    path('categorias/excluir/<int:pk>/', views.excluir_categoria, name='excluir_categoria'),
    path('tags/', views.listar_tags, name='listar_tags'),
    path('tags/nova/', views.cadastrar_tag, name='cadastrar_tag'),
    path('tags/editar/<int:pk>/', views.atualizar_tag, name='atualizar_tag'),
]