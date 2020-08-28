from rest_framework import serializers
from .models import Pessoa, Departamento

class PessoaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pessoa
        fields = ('id', 'nome', 'salario', 'data_nascimento')

class DepartamentoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Departamento
        fields = ('id', 'sigla')