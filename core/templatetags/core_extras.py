from django import template

register = template.Library()


@register.simple_tag()
def saldo_final(saldo, taxa, *args, **kwargs):
    acrescimo = float(saldo) * float((taxa / 100))
    return saldo + acrescimo
