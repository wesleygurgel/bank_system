from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView


# Create your views here.

class IndexView(TemplateView):
    template_name = 'index.html'


class ContaView(TemplateView):
    template_name = 'conta.html'
