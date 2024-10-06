from django.db import models

class Prioridade(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao

class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Tarefa(models.Model):
    descricao = models.CharField(max_length=255)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    prioridade = models.ForeignKey(Prioridade, on_delete=models.CASCADE)
    feito = models.CharField(max_length=1)

    def __str__(self):
        return self.descricao
