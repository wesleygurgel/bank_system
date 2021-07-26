from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Base(models.Model):
    criados = models.DateField('Criação', auto_now_add=True)
    modificado = models.DateField('Atualização', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True


class TipoConta(Base):
    tipo_conta = models.CharField('Tipo Conta', max_length=100)

    class Meta:
        verbose_name = 'Tipo de Conta'
        verbose_name_plural = 'Tipos de Conta'

    def __str__(self):
        return self.tipo_conta


class Conta(Base):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    tipo_conta = models.ForeignKey(TipoConta, related_name='conta_tipo', on_delete=models.CASCADE)
    proprietario = models.CharField('Proprietário', max_length=100)
    credito = models.DecimalField('Crédito', max_digits=7, decimal_places=2)
    saldo = models.FloatField(default=0.0)

    class Meta:
        verbose_name = 'Conta'

    def __str__(self):
        return f'Número da Conta:{self.id}\nProprietário: {self.proprietario}\nSaldo: {self.saldo}'

    def transferir(self, destino, valor):
        conta_destino = Conta.objects.get(id=destino)
        print(conta_destino)
        self.saldo -= valor
        destino.saldo += valor
