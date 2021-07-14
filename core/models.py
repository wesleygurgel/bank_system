from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Base(models.Model):
    criados = models.DateField('Criação', auto_now_add=True)
    modificado = models.DateField('Atualização', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True


class Conta(Base):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    proprietario = models.CharField('Proprietário', max_length=100)
    credito = models.DecimalField('Crédito', max_digits=3, decimal_places=2)
    saldo = models.FloatField(default=0.0)

    class Meta:
        verbose_name = 'Conta'

    def __str__(self):
        return f'Número da Conta:{self.id}\nProprietário: {self.proprietario}\nSaldo: {self.saldo}'







