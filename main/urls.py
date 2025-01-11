from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('dados/', dados, name='dados'),
    path('contatos/', contatos, name='contatos'),
    path('historia/', historia, name='historia'),
    path('curiosidades/', curiosidades, name='curiosidades'),
    path('faça-sua-parte/', faça_sua_parte, name='faça-sua-parte'),
    path('especies/', especies, name='especies'),
    path('listagem/', listagem, name='listagem'),
    path('cadastrar/animal/', cadastrar, name='cadastrar'),
    path('editar/animal/<int:id>/', editar, name='editar'),
    path('deletar/animal/<int:id>/', deletar, name='deletar'),
    # path('cadastrar/artigo/', cadastrar_artigo, name='cadastrar_artigo'),
    # path('editar/artigo/<int:id>/', editar_artigo, name='editar_artigo'),
    # path('deletar/artigo/<int:id>/', deletar_artigo, name='deletar_artigo'),
]
