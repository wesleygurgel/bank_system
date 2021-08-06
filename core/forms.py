from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from .models import ContaBonus, ContaPoupanca, Conta


class CadastrarForm(forms.Form):
    CHOICES = (
        ('Conta Bônus', 'Conta Bônus'),
        ('Conta Poupança', 'Conta Poupança')
    )

    proprietario = forms.CharField(label='Proprietário', max_length=100)
    tipo_conta = forms.ChoiceField(choices=CHOICES)
    credito = forms.DecimalField(label='Crédito')
    saldo = forms.DecimalField(label='Saldo')

    def criar_conta(self, user_id):
        usuario = User.objects.get(id=user_id)
        proprietario = self.cleaned_data['proprietario']
        tipo_cleaned = self.cleaned_data['tipo_conta']
        credito = self.cleaned_data['credito']
        saldo = self.cleaned_data['saldo'] + credito

        print(f'Criando Conta para o login: {usuario}')
        if tipo_cleaned == 'Conta Bônus':
            ContaBonus.objects.create(usuario=usuario, proprietario=proprietario, pontuacao=10, credito=credito,
                                      saldo=saldo, tipo=tipo_cleaned)
            print('Conta Bônus criada!')

        else:
            ContaPoupanca.objects.create(usuario=usuario, proprietario=proprietario, taxa_juros=0, credito=credito,
                                         saldo=saldo, tipo=tipo_cleaned)
            print('Conta Poupança Criada!')


class DepositoForm(forms.Form):
    valor = forms.FloatField(label='Valor')

    def realizar_deposito(self, conta):
        valor = self.cleaned_data['valor']
        print(f'Valor depósito: {valor}')

        if valor >= 150 and conta.tipo == "Conta Bônus":
            pontuacao_encrease = valor // 150
            conta.contabonus.pontuacao += int(pontuacao_encrease)
            conta.contabonus.save()

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

        if valor_transferir >= 200 and conta_destino.tipo == 'Conta Bônus':
            conta_destino.contabonus.pontuacao += int(valor_transferir // 200)
            conta_destino.contabonus.save()

        conta.saldo -= valor_transferir
        conta_destino.saldo += valor_transferir

        conta.save()
        conta_destino.save()


class RenderJurosForm(forms.Form):
    taxa_juros = forms.DecimalField(label='Taxa de Juros', max_digits=2)

    def atualizar_taxa_juros(self, contas):
        for conta in contas:
            if conta.tipo == 'Conta Poupança':
                conta.contapoupanca.taxa_juros = self.cleaned_data['taxa_juros']
                conta.contapoupanca.save()
