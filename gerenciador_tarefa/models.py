from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Tarefa(models.Model):
    PRIORIDADE_OPCOES = [
        ('N', 'Normal'),
        ('A', 'Alta'),
        ('B', 'Baixa')
    ]
    titulo = models.CharField(max_length=30, null=False, blank=False, verbose_name='Título')
    descricao = models.CharField(max_length=100, null=False, blank=False, verbose_name='Descrição')
    data_expiracao = models.DateField(null=False, blank=False, verbose_name='Data de Expiração')
    prioridade = models.CharField(max_length=1, choices=PRIORIDADE_OPCOES, null=False, blank=False, verbose_name='Prioridade')
    usuario = models.ForeignKey(User, verbose_name='Usuário', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Tarefas'

    def __str__(self):
        return self.titulo
