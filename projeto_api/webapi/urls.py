from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'contaspagar', views.ContasPagarViewSet)
router.register(r'contasreceber', views.ClassificacaoViewSet)
router.register(r'classificacao', views.ClassificacaoViewSet)
router.register(r'formapagamento', views.FormaPagamentoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]