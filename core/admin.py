from django.contrib import admin
from .models import Conta, TipoConta


# Register your models here.

@admin.register(Conta)
class ContaAdmin(admin.ModelAdmin):
    list_display = ['id', 'proprietario', 'saldo', 'criados', 'ativo']


@admin.register(TipoConta)
class TipoContaAdmin(admin.ModelAdmin):
    list_display = ['tipo_conta', 'criados', 'modificado', 'ativo']
