from django.contrib import admin
from django.urls import path
from ListaDeTarefas import views

urlpatterns = [
    path('', views.listaTarefas, name='listaTarefas'),
    path('tarefas/excluir/<int:id>/', views.excluirTarefa, name='excluirTarefa'),
    path('feito/<int:tarefa_id>/', views.marcar_como_feito, name='marcarComoFeito'),
    path('categorias/', views.listaCategorias, name='listaCategorias'),
    path('categoria/excluir/<int:id>/', views.excluirCategoria, name='excluirCategoria'),
    path('prioridades/', views.listaPrioridades, name='listaPrioridades'),
    path('prioridades/excluir/<int:id>/', views.excluirPrioridade, name='excluirPrioridade'),
]
