from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView


# Create your views here.

class IndexView(TemplateView):
    template_name = 'index.html'


class LoginView(TemplateView):
    template_name = 'login.html'
