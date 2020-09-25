from django.contrib import admin
from .models import SaldoInicial, ContasPagar, ContasReceber, Classificacao, FormaPagamento


# Register your models here.
admin.site.register(SaldoInicial)
admin.site.register(ContasPagar)
admin.site.register(ContasReceber)
admin.site.register(Classificacao)
admin.site.register(FormaPagamento)
