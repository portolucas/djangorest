from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'saldoinicial', views.SaldoInicialViewSet)
router.register(r'contaspagar', views.ContasPagarViewSet)
router.register(r'contasreceber', views.ContasReceberViewSet)
router.register(r'classificacao', views.ClassificacaoViewSet)
router.register(r'formapagamento', views.FormaPagamentoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('relatorio-data-vencimento/<str:date>/', views.relatorio_data_vencimento),
    path('fluxo-de-caixa/<str:start_date>/<str:end_date>/<int:classif>/', views.fluxo_de_caixa),
    path('fluxo-previsto/<str:start_date>/', views.fluxo_previsto),
    path('fluxo-realizado/<str:start_date>/', views.fluxo_realizado)
]