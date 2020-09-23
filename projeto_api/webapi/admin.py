from django.contrib import admin
from .models import ContasPagar, ContasReceber, Classificacao, FormaPagamento


# Register your models here.

admin.site.register(ContasPagar)
admin.site.register(ContasReceber)
admin.site.register(Classificacao)
admin.site.register(FormaPagamento)
