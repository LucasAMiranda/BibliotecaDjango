from django.db import models
from datetime import date


# Herança models herda de Model

class Livros(models.Model):
    nome = models.CharField(max_length=100)
    autor = models.CharField(max_length=30)
    co_autor = models.CharField(max_length=30, blank=True)
    data_cadastro = models.DateField(default=date.today())
    emprestado = models.BooleanField(default=False, null=True)
    nome_emprestado = models.CharField(max_length=30, blank=True, null=True)
    data_emprestimo = models.DateTimeField(blank=True, null=True)
    data_devolucao = models.DateTimeField(blank=False, null=True)

    class Meta:
        verbose_name = 'Livro'

    def __str__(self):
        return self.nome
