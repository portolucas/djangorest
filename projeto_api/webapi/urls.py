from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'pessoa', views.PessoaViewSet)
router.register(r'departamento', views.DepartamentoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]