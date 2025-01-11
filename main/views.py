from django.shortcuts import render

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