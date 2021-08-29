from django.test import TestCase
import core.models as model
from django.contrib.auth.models import User


class ModelTesting(TestCase):

    def setUp(self) -> None:
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

        self.bonus = model.ContaBonus.objects.create(
            usuario=self.user,
            proprietario='Raul Souto',
            credito=500,
            saldo=2500,
            tipo='Conta Bônus',
            pontuacao=10
        )

    def test_post_model_poupanca(self):
        conta_criada = self.poupanca
        self.assertTrue(isinstance(conta_criada, model.ContaPoupanca))

    def test_post_model_bonus(self):
        conta_criada = self.bonus
        self.assertTrue(isinstance(conta_criada, model.ContaBonus))

    def test_transferir(self):
        saldo_antigo = self.poupanca.saldo
        self.poupanca.transferir(self.bonus, 200)
        saldo_novo = self.poupanca.saldo

        self.assertEquals(saldo_novo + 200, saldo_antigo)

    def test_str(self):
        self.assertEqual(str(self.poupanca), f'Número da Conta:{self.poupanca.id}\nProprietário: '
                                        f'{self.poupanca.proprietario}\nSaldo:'
                                        f' {self.poupanca.saldo}')

        self.assertEqual(str(self.bonus), f'Número da Conta:{self.bonus.id}\nProprietário: '
                                             f'{self.bonus.proprietario}\nSaldo:'
                                             f' {self.bonus.saldo}')
