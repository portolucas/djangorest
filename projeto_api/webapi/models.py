from django.db import models

# Create your models here.
class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    salario = models.DecimalField(
        max_digits=7, decimal_places=2
    )
    data_nascimento = models.DateTimeField()

    def __str__(self):
        return self.nome

class Departamento(models.Model):
    nome = models.CharField(max_length=30)
    sigla = models.CharField(max_length=6)