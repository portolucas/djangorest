from django.shortcuts import render
from rest_framework import viewsets
from .models import Pessoa, Departamento
from .serializers import PessoaSerializer, DepartamentoSerializer
# Create your views here.

class PessoaViewSet(viewsets.ModelViewSet):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer

class DepartamentoViewSet(viewsets.ModelViewSet):
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer
