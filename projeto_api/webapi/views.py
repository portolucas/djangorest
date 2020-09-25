from django.shortcuts import render
import datetime
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework import filters
from rest_framework.decorators import action, api_view
from rest_framework import generics
from .models import SaldoInicial, ContasPagar, ContasReceber, Classificacao, FormaPagamento
from .serializers import SaldoInicialSerializer, ContasPagarSerializer, ContasReceberSerializer, ClassificacaoSerializer, FormaPagamentoSerializer
# Create your views here.


class SaldoInicialViewSet(viewsets.ModelViewSet):
    queryset = SaldoInicial.objects.all()
    serializer_class = SaldoInicialSerializer


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


@api_view(['GET'])
def relatorio_data_vencimento(request, date):
    a_pagar = ContasPagar.objects.filter(data_vencimento=date)
    a_receber = ContasReceber.objects.filter(data_expectativa=date)

    serializer_pagar = ContasPagarSerializer(a_pagar, many=True)
    serializer_receber = ContasReceberSerializer(a_receber, many=True)

    response_api = {'À pagar': serializer_pagar.data,
                    'À receber': serializer_receber.data}

    return Response(response_api, status=status.HTTP_200_OK)


@api_view(['GET'])
def fluxo_de_caixa(request, start_date, end_date, classif):

    saldo_inicial = SaldoInicial.objects.filter(pk=1)
    recebidos = ContasReceber.objects.filter(
        data_recebimento__gte=start_date, data_recebimento__lte=end_date, situacao='pago', classificacao=classif)
    pagos = ContasPagar.objects.filter(
        data_pagamento__gte=start_date, data_pagamento__lte=end_date, situacao='pago', classificacao=classif)

    serializer_saldo_inicial = SaldoInicialSerializer(
        saldo_inicial, many=True)

    serializer_pagos = ContasPagarSerializer(pagos, many=True)

    serializer_recebidos = ContasReceberSerializer(recebidos, many=True)

    valor_recebidos = []
    valor_pagos = []
    saldo_inicial_value = 0

    for x in saldo_inicial:
        saldo_inicial_value = x.saldo

    for x in recebidos:
        valor_recebidos.append(x.valor)

    for x in pagos:
        valor_pagos.append(x.valor)

    def reduce(function, iterable, initilizer=None):
        it = iter(iterable)
        if initilizer is None:
            value = next(it)
        else:
            value = initilizer
        for element in it:
            value = function(value, element)
        return value

    def sum(a, b):
        result = a + b
        return result

    if valor_recebidos:
        total_recebidos = reduce(sum, valor_recebidos)
    else:
        total_recebidos = 0
    if valor_pagos:
        total_pagos = reduce(sum, valor_recebidos)
    else:
        total_pagos = 0

    lucratividade = (saldo_inicial_value + total_recebidos) - total_pagos

    response_api = [{"período": [{"inicio": start_date, "fim": end_date}], "saldo inicial": serializer_saldo_inicial.data, "total_recebidos": total_recebidos,
                     "total_pagos": total_pagos, "pagos": serializer_pagos.data, "recebidos": serializer_recebidos.data, "lucratividade": lucratividade}]

    return Response(response_api, status=status.HTTP_200_OK)


@api_view(['GET'])
def fluxo_previsto(request, start_date):
    a_receber = ContasReceber.objects.filter(
        data_recebimento__gte=start_date, situacao='pagar')
    a_pagar = ContasPagar.objects.filter(
        data_pagamento__gte=start_date, situacao='pagar')

    serializer_receber = ContasReceberSerializer(a_receber, many=True)
    serializer_pagar = ContasPagarSerializer(a_pagar, many=True)

    response_api = [{"período": start_date,
                     "a receber": serializer_receber.data, "a pagar": serializer_pagar.data}]

    return Response(response_api, status=status.HTTP_200_OK)


@api_view(['GET'])
def fluxo_realizado(request, start_date):
    recebidos = ContasReceber.objects.filter(
        data_recebimento__gte=start_date, situacao='pago')
    pagos = ContasPagar.objects.filter(
        data_pagamento__gte=start_date, situacao='pago')

    serializer_pagos = ContasPagarSerializer(pagos, many=True)

    serializer_recebidos = ContasReceberSerializer(recebidos, many=True)

    response_api = [{"período": start_date, "recebido": serializer_pagos.data,
                     "pago": serializer_recebidos.data}]

    return Response(response_api, status=status.HTTP_200_OK)
