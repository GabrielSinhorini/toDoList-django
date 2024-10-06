from django.shortcuts import render, redirect, get_object_or_404
from .models import Tarefa, Categoria, Prioridade
from .forms import CategoriaForm, PrioridadeForm, TarefaForm

def listaTarefas(request):
    tarefas = Tarefa.objects.all()
    categorias = Categoria.objects.all()
    prioridades = Prioridade.objects.all()

    if request.method == 'POST':
        tarefa_id = request.POST.get('id')
        nome = request.POST.get('nome')
        categoria_id = request.POST.get('categoria')
        prioridade_id = request.POST.get('prioridade')

        categoria = get_object_or_404(Categoria, id=categoria_id)
        prioridade = get_object_or_404(Prioridade, id=prioridade_id)

        if tarefa_id:
            tarefa = get_object_or_404(Tarefa, id=tarefa_id)
            tarefa.descricao = nome
            tarefa.categoria = categoria
            tarefa.prioridade = prioridade
            tarefa.save()
        else:
            nova_tarefa = Tarefa(descricao=nome, categoria=categoria, prioridade=prioridade)
            nova_tarefa.save()

        return redirect('listaTarefas')

    if 'id' in request.GET:
        tarefa = get_object_or_404(Tarefa, id=request.GET['id'])
    else:
        tarefa = None

    return render(request, 'html/tarefas.html', {
        'tarefas': tarefas,
        'categorias': categorias,
        'prioridades': prioridades,
        'tarefa': tarefa
    })

def marcar_como_feito(request, tarefa_id):
    tarefa = get_object_or_404(Tarefa, id=tarefa_id)
    
    if tarefa.feito == 'S':
        tarefa.feito = 'N'
    else:
        tarefa.feito = 'S'

    tarefa.save()
    return redirect('listaTarefas')

def excluirTarefa(request, id):
    tarefa = get_object_or_404(Tarefa, id=id)
    tarefa.delete()
    return redirect('listaTarefas')

def listaCategorias(request):
    categorias = Categoria.objects.all()

    form = CategoriaForm()

    if request.method == 'POST':
        if 'id' in request.POST and request.POST['id']:
            categoria = get_object_or_404(Categoria, id=request.POST['id'])
            form = CategoriaForm(request.POST, instance=categoria)
        else:
            form = CategoriaForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('listaCategorias')

    if 'id' in request.GET and request.GET['id']:
        categoria = get_object_or_404(Categoria, id=request.GET['id'])
        form = CategoriaForm(instance=categoria)

    return render(request, 'html/categorias.html', {'categorias': categorias, 'form': form})

def excluirCategoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    categoria.delete()
    return redirect('listaCategorias')

def listaPrioridades(request):
    prioridades = Prioridade.objects.all()

    if request.method == 'POST':
        if 'id' in request.POST and request.POST['id']:
            prioridade = get_object_or_404(Prioridade, id=request.POST['id'])
            form = PrioridadeForm(request.POST, instance=prioridade)
        else:
            form = PrioridadeForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('listaPrioridades')
        else:
            print(form.errors)

    else:
        if 'id' in request.GET and request.GET['id']:
            prioridade = get_object_or_404(Prioridade, id=request.GET['id'])
            form = PrioridadeForm(instance=prioridade)
        else:
            form = PrioridadeForm()

    return render(request, 'html/prioridades.html', {'prioridades': prioridades, 'form': form})

def excluirPrioridade(request, id):
    prioridade = get_object_or_404(Prioridade, id=id)
    prioridade.delete()
    return redirect('listaPrioridades')
