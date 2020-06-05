from django.urls import path
from .views import tarefa_views
from .views import usuario_views

urlpatterns = [
    path('', tarefa_views.listar_tarefas, name='listar_tarefas'),
    path('cadastrar/', tarefa_views.cadastrar_tarefa, name='cadastrar_tarefas'),
    path('editar/<int:id>', tarefa_views.editar_tarefa, name='editar_tarefa'),
    path('remover/<int:id>', tarefa_views.remover_tarefa, name='remover_tarefa'),
    path('cadastrar_usuario/', usuario_views.cadastrar_usuario, name='cadastrar_usuario'),
    path('login/', usuario_views.logar_usuario, name='logar_usuario'),
    path('deslogar_usario', usuario_views.deslogar_usuario, name='deslogar_usuario'),
]