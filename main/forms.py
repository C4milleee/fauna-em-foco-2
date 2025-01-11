from django import forms
from .models import Especie, Artigo

class EspecieForm(forms.ModelForm):
  class Meta:
    model = Especie
    fields = '__all__'

class ArtigoForm(forms.ModelForm):
  class Meta:
    model = Artigo
    fields = '__all__'