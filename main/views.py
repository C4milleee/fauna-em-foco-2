from django.shortcuts import render, redirect, get_object_or_404
from .models import Especie, Artigo
from .forms import EspecieForm, ArtigoForm

def home(request):
    return render(request, 'home.html')

def dados(request):
    return render(request, 'dados.html')

def contatos(request):
    return render(request, 'contatos.html')

def historia(request):
    return render(request, 'historia.html')

def curiosidades(request):
    return render(request, 'curiosidades.html')


def faça_sua_parte(request):
    return render(request, 'faça-sua-parte.html')


def especies(request):
    return render(request, 'especies.html')

def listagem(request):
    especies = Especie.objects.all()
    artigos = Artigo.objects.all()
    context = {
        'especies': especies,
        'artigos': artigos
    }
    return render(request, 'listagem_animais.html', context)
    

def cadastrar(request):
    if request.method == 'POST':
        form = EspecieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listagem')
    else:
        form = EspecieForm()
    
    return render(request, 'cadastrar_animal.html', {'form': form})


def editar(request, id):
    especie = get_object_or_404(Especie, pk=id)
    if request.method == 'POST':
        form = EspecieForm(request.POST, instance=especie)
        if form.is_valid():
            form.save()
            return redirect('listagem') 
    else:
        form = EspecieForm(instance=especie)
    
    return render(request, 'editar_animal.html', {'form': form})


def deletar(request, id):
  especie = get_object_or_404(Especie, pk=id)
  if request.method == 'POST':
    especie.delete()
    return redirect('listagem') 
  return render(request, 'deletar_animal.html')

def cadastrar_artigo(request):
    if request.method == 'POST':
        form = ArtigoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listagem')
    else:
        form = ArtigoForm()
    
    return render(request, 'cadastrar_artigo.html', {'form': form})


def editar_artigo(request, id):
    artigo = get_object_or_404(Artigo, pk=id)
    if request.method == 'POST':
        form = ArtigoForm(request.POST, instance=artigo)
        if form.is_valid():
            form.save()
            return redirect('listagem') 
    else:
        form = ArtigoForm(instance=artigo)
    
    return render(request, 'editar_artigo.html', {'form': form})


def deletar_artigo(request, id):
  artigo = get_object_or_404(Artigo, pk=id)
  if request.method == 'POST':
    artigo.delete()
    return redirect('listagem') 
  return render(request, 'deletar_artigo.html')