from django.db import models
from django.contrib.auth.models import User
# from django.contrib.contenttypes.fields import GenericForeignKey
# from django.contrib.contenttypes.models import ContentType


# Create your models here.

class Base(models.Model):
    criados = models.DateField('Criação', auto_now_add=True)
    modificado = models.DateField('Atualização', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True


class Conta(Base):

    CHOICES = (
        ('Conta Bônus', 'Conta Bônus'),
        ('Conta Poupança', 'Conta Poupança')
    )

    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    proprietario = models.CharField('Proprietário', max_length=100)
    credito = models.DecimalField('Crédito', max_digits=7, decimal_places=2)
    saldo = models.FloatField(default=0.0)
    tipo = models.CharField('Tipo de Conta', choices=CHOICES, max_length=20)

    class Meta:
        verbose_name = 'Conta'

    def __str__(self):
        return f'Número da Conta:{self.id}\nProprietário: {self.proprietario}\nSaldo: {self.saldo}'

    def transferir(self, destino, valor):
        self.saldo -= valor
        destino.saldo += valor


class ContaBonus(Conta):
    pontuacao = models.DecimalField('Pontuação', decimal_places=2, max_digits=100)

    class Meta:
        verbose_name = 'Conta Bônus'

    def __str__(self):
        return super(ContaBonus, self).__str__()


class ContaPoupanca(Conta):
    taxa_juros = models.DecimalField('Taxa de Juros', max_digits=4, decimal_places=2)

    class Meta:
        verbose_name = 'Conta Poupança'

    def __str__(self):
        return super(ContaPoupanca, self).__str__()
