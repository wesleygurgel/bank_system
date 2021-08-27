from django.test import TestCase
import core.models as model
from django.contrib.auth.models import User


class TestModels(TestCase):

    def setUp(self):
        self.user = User.objects.create_user('username', 'user@gmail.com', 'password')
        self.user.save()

        self.poupanca = model.ContaPoupanca.objects.create(
            usuario=self.user,
            proprietario='Luiz Eduardo',
            credito=200,
            saldo=1200,
            tipo='Conta Poupança',
            taxa_juros=1
        )

        self.poupanca2 = model.ContaPoupanca.objects.create(
            usuario=self.user,
            proprietario='Hilton Kevin Carvalho',
            credito=200,
            saldo=1200,
            tipo='Conta Poupança',
            taxa_juros=1
        )

    def test_poupanca_transferir(self):
        saldo_antigo = self.poupanca.saldo
        self.poupanca.transferir(self.poupanca2, 200)
        saldo_novo = self.poupanca.saldo

        self.assertEquals(saldo_novo + 200, saldo_antigo)


