from django.shortcuts import render
from rest_framework import viewsets
from .models import ContasPagar, ContasReceber, Classificacao, FormaPagamento
from .serializers import ContasPagarSerializer, ContasReceberSerializer, ClassificacaoSerializer, FormaPagamentoSerializer
# Create your views here.


class ContasPagarViewSet(viewsets.ModelViewSet):
    queryset = ContasPagar.objects.all()
    serializer_class = ContasPagarSerializer

class ContasReceberViewSet(viewsets.ModelViewSet):
    queryset = ContasReceber.objects.all()
    serializer_class = ContasReceberSerializer

class ClassificacaoViewSet(viewsets.ModelViewSet):
    queryset = Classificacao.objects.all()
    serializer_class = ClassificacaoSerializer

class FormaPagamentoViewSet(viewsets.ModelViewSet):
    queryset = FormaPagamento.objects.all()
    serializer_class = FormaPagamentoSerializer

