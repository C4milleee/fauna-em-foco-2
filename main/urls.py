from django.urls import path
from .views import home, dados, contatos, historia, curiosidades, especies, faça_sua_parte

urlpatterns = [
    path('', home, name='home'),
    path('dados/', dados, name='dados'),
    path('contatos/', contatos, name='contatos'),
    path('historia/', historia, name='historia'),
    path('curiosidades/', curiosidades, name='curiosidades'),
    path('faça-sua-parte/', faça_sua_parte, name='faça-sua-parte'),
    path('especies/', especies, name='especies'),
]
