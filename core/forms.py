from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from .models import Conta


class CadastrarForm(forms.Form):
    Usuario = get_user_model()
    usuarios = []
    for user in Usuario.objects.all():
        usuario_tuple = (str(user), str(user))
        usuarios.insert(0, usuario_tuple)

    print(usuarios)
    print(type(usuarios))

    usuario = forms.ChoiceField(choices=usuarios)
    proprietario = forms.CharField(label='Proprietário', max_length=100)
    credito = forms.DecimalField(label='Crédito', max_digits=7, decimal_places=2)
    saldo = forms.DecimalField(label='Saldo', decimal_places=2)

    def criar_conta(self):
        print('tentar criar conta')
        usuario = User.objects.get(username=self.cleaned_data['usuario'])
        proprietario = self.cleaned_data['proprietario']
        credito = self.cleaned_data['credito']
        saldo = self.cleaned_data['saldo']

        print(f'Meu usuario é {usuario}, type: {type(usuario)}')

        Conta.objects.create(usuario=usuario, proprietario=proprietario, credito=credito, saldo=saldo)
