from rest_framework import serializers
from .models import SaldoInicial, ContasPagar, Classificacao, FormaPagamento, ContasReceber


class SaldoInicialSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaldoInicial
        fields = ('id', 'saldo')

class ContasPagarSerializer(serializers.ModelSerializer):

    class Meta:
        model = ContasPagar
        fields = ('id', 'data_vencimento', 'data_pagamento', 'valor',
                  'descricao', 'classificacao', 'forma_pagamento', 'situacao')


class ContasReceberSerializer(serializers.ModelSerializer):

    class Meta:
        model = ContasReceber
        fields = ('id', 'data_expectativa', 'data_recebimento', 'valor',
                  'descricao', 'classificacao', 'forma_recebimento', 'situacao')


class ClassificacaoSerializer(serializers.ModelSerializer):

    classificacao_cp = serializers.PrimaryKeyRelatedField(
        many=True, read_only=True, allow_null=True, required=False)
    classificacao_cr = serializers.PrimaryKeyRelatedField(
        many=True, read_only=True, allow_null=True, required=False)

    class Meta:
        model = Classificacao
        fields = ('id', 'descricao', 'classificacao_cp', 'classificacao_cr')


class FormaPagamentoSerializer(serializers.ModelSerializer):

    forma_pagamento_cp = serializers.PrimaryKeyRelatedField(
        many=True, read_only=True, allow_null=True, required=False)
    forma_recebimento_cr = serializers.PrimaryKeyRelatedField(
        many=True, read_only=True, allow_null=True, required=False)

    class Meta:
        model = FormaPagamento
        fields = ('id', 'descricao', 'forma_pagamento_cp', 'forma_recebimento_cr')
