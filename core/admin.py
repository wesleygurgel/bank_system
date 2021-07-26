from django.contrib import admin
from .models import Conta, ContaBonus, ContaPoupanca


# Register your models here.

@admin.register(Conta)
class ContaAdmin(admin.ModelAdmin):
    list_display = ['id', 'proprietario', 'contabonus', 'contapoupanca', 'saldo', 'criados', 'ativo']
    # list_display = [field.name for field in Conta._meta.get_fields()]


@admin.register(ContaBonus)
class ContaBonusAdmin(admin.ModelAdmin):
    list_display = ['id', 'proprietario', 'saldo', 'pontuacao', 'criados', 'ativo']


@admin.register(ContaPoupanca)
class ContaPoupancaAdmin(admin.ModelAdmin):
    list_display = ['id', 'proprietario', 'saldo', 'taxa_juros', 'criados', 'ativo']
