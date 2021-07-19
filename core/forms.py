from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from .models import Conta


class CadastrarForm(forms.Form):

    proprietario = forms.CharField(label='Proprietário', max_length=100)
    credito = forms.DecimalField(label='Crédito')
    saldo = forms.DecimalField(label='Saldo')

    def criar_conta(self, user_id):
        usuario = User.objects.get(id=user_id)
        proprietario = self.cleaned_data['proprietario']
        credito = self.cleaned_data['credito']
        saldo = self.cleaned_data['saldo']

        print(f'Criando Conta para o login: {usuario}')
        Conta.objects.create(usuario=usuario, proprietario=proprietario, credito=credito, saldo=saldo)


class DepositoForm(forms.Form):
    valor = forms.FloatField(label='Valor')

    def realizar_deposito(self, conta):
        valor = self.cleaned_data['valor']
        print(f'Saldo Antigo: {conta.saldo}')
        conta.saldo += valor
        print(f'Saldo Novo: {conta.saldo}')
        conta.save()


class TransferirForm(forms.Form):
    numero_conta = forms.DecimalField(label='Numero da Conta')
    valor_transferir = forms.FloatField(label='Valor')

    def transferir(self, conta):
        numero_conta = self.cleaned_data['numero_conta']
        valor_transferir = self.cleaned_data['valor_transferir']
        conta_destino = Conta.objects.get(id=numero_conta)

        conta.saldo -= valor_transferir
        conta_destino.saldo += valor_transferir

        conta.save()
        conta_destino.save()




