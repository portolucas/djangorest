from django.db import models

# Create your models here.


class SaldoInicial(models.Model):
    saldo = models.DecimalField(max_digits=9, decimal_places=2)
    
    def __str__(self):
        return (self.saldo)


class Classificacao(models.Model):
    descricao = models.CharField(max_length=100, null=True)

    def __str__(self):
        return (self.descricao)


class FormaPagamento(models.Model):
    descricao = models.CharField(max_length=50, null=True)

    def __str__(self):
        return (self.descricao)


class ContasPagar(models.Model):
    data_vencimento = models.DateField()
    data_pagamento = models.DateField(null=True)
    valor = models.DecimalField(max_digits=7, decimal_places=2)
    classificacao = models.ForeignKey(
        Classificacao, related_name='classificacao_cp',  on_delete=models.RESTRICT, null=True)
    descricao = models.CharField(max_length=100)
    forma_pagamento = models.ForeignKey(
        FormaPagamento, related_name='forma_pagamento_cp', on_delete=models.RESTRICT, null=True)
    situacao = models.CharField(max_length=50, null=True)
    
    def __str__(self):
        return (self.descricao)


class ContasReceber(models.Model):
    data_expectativa = models.DateField()
    data_recebimento = models.DateField(null=True)
    valor = models.DecimalField(max_digits=7, decimal_places=2)
    descricao = models.CharField(max_length=100)
    classificacao = models.ForeignKey(
        Classificacao, related_name='classificacao_cr',  on_delete=models.RESTRICT, null=True)
    forma_recebimento = models.ForeignKey(
        FormaPagamento, related_name='forma_recebimento_cr', on_delete=models.RESTRICT, null=True)
    situacao = models.CharField(max_length=50, null=True)
    
    def __str__(self):
        return (self.descricao)
