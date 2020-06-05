from django.http import HttpResponse
from django.shortcuts import render, redirect
from gerenciador_tarefa.forms import TarefaForm
from gerenciador_tarefa.entidades import tarefa
from gerenciador_tarefa.services import tarefa_services
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def listar_tarefas(request):
    tarefas = tarefa_services.listar_tarefas(request.user)
    return render(request, 'tarefas/listar_tarefas.html', {'tarefas': tarefas, 'listagem_page': 'active'})

@login_required
def cadastrar_tarefa(request):
    if request.method == 'POST':
        form_tarefa = TarefaForm(request.POST)
        if form_tarefa.is_valid():
            titulo = form_tarefa.cleaned_data['titulo']
            descricao = form_tarefa.cleaned_data['descricao']
            data_expiracao = form_tarefa.cleaned_data['data_expiracao']
            prioridade = form_tarefa.cleaned_data['prioridade']
            nova_tarefa = tarefa.Tarefa(titulo=titulo,
                                        descricao=descricao,
                                        data_expiracao=data_expiracao,
                                        prioridade=prioridade,
                                        usuario=request.user)

            tarefa_services.cadastrar_tarefa(nova_tarefa)
            return redirect('listar_tarefas')
    else:
        form_tarefa = TarefaForm()
    return render(request, 'tarefas/form_tarefa.html', {'form_tarefa': form_tarefa, 'cadastro_page': 'active'})

@login_required
def editar_tarefa(request, id):
    tarefa_bd = tarefa_services.listar_tarefa_id(id)
    if tarefa_bd.usuario != request.user:
        return HttpResponse('Não permitido')
    form_tarefa = TarefaForm(request.POST or None, instance=tarefa_bd)
    if form_tarefa.is_valid():
        titulo = form_tarefa.cleaned_data['titulo']
        descricao = form_tarefa.cleaned_data['descricao']
        data_expiracao = form_tarefa.cleaned_data['data_expiracao']
        prioridade = form_tarefa.cleaned_data['prioridade']
        nova_tarefa = tarefa.Tarefa(titulo=titulo,
                                    descricao=descricao,
                                    data_expiracao=data_expiracao,
                                    prioridade=prioridade,
                                    usuario=request.user)

        tarefa_services.editar_tarefa(tarefa_bd, nova_tarefa)
        return redirect('listar_tarefas')
    return render(request, 'tarefas/form_tarefa.html', {'form_tarefa': form_tarefa})

@login_required
def remover_tarefa(request, id):
    tarefa_bd = tarefa_services.listar_tarefa_id(id)
    if tarefa_bd.usuario != request.user:
        return HttpResponse('Não permitido')
    if request.method == 'POST':
        tarefa_services.remover_tarefa(tarefa_bd)
        return redirect('listar_tarefas')
    return render(request, 'tarefas/confirma_exclusao.html', {'tarefa': tarefa_bd})