from django.contrib import admin
from .models import Pessoa, Departamento


# Register your models here.
admin.site.register(Pessoa)
admin.site.register(Departamento)