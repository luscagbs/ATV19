from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Categoria
from django.db.models.deletion import ProtectedError

def listar_categorias(request):
    categorias = Categoria.objects.all()

    return render(request, 'portal/categorias/lista.html', {
        'categorias': categorias
    })


def cadastrar_categoria(request):
    if request.method == 'POST':
        nome = request.POST.get('nome', '').strip()

        if nome:
            Categoria.objects.create(nome=nome)
            messages.success(request, 'Categoria cadastrada com sucesso!')
            return redirect('listar_categorias')
        else:
            messages.error(request, 'O nome da categoria é obrigatório.')

    return render(request, 'portal/categorias/formulario.html')


def atualizar_categoria(request, pk):
    categoria = Categoria.objects.filter(pk=pk).first()

    if request.method == 'POST':
        nome = request.POST.get('nome', '').strip()

        if nome:
            categoria.nome = nome
            categoria.save()

            messages.success(request, 'Categoria atualizada com sucesso!')
            return redirect('listar_categorias')
        else:
            messages.error(request, 'O nome da categoria é obrigatório.')

    return render(request, 'portal/categorias/formulario.html', {
        'categoria': categoria
    })

def inicio(request):
    return render(request, 'portal/inicio.html')

def excluir_categoria(request, pk):
    categoria = Categoria.objects.filter(pk=pk).first()

    if request.method == 'POST':
        try:
            categoria.delete()
            messages.success(request, 'Categoria excluída com sucesso!')
        except ProtectedError:
            messages.error(
                request,
                'Não é possível excluir esta categoria, pois existem notícias vinculadas a ela.'
            )

        return redirect('listar_categorias')

    return render(request, 'portal/categorias/excluir.html', {
        'categoria': categoria
    })