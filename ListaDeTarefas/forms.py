from django import forms
from .models import Categoria, Prioridade, Tarefa

class TarefaForm(forms.ModelForm):
    class Meta:
        model = Tarefa
        fields = ['descricao', 'categoria', 'prioridade']

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nome']

class PrioridadeForm(forms.ModelForm):
    class Meta:
        model = Prioridade
        fields = ['descricao']
