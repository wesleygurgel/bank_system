from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView, FormView
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy
from .models import Conta
from django.contrib import messages


# Create your views here.

class IndexView(TemplateView):
    template_name = 'index.html'


class LoginView(View):
    def get(self, request, *args, **kwargs):
        if str(request.user) == 'AnonymousUser':
            return render(request, 'login.html')
        else:
            return redirect('/conta/')


class SubmitLoginView(View):
    def post(self, request):
        username = request.POST.get('username')
        print(username)
        password = request.POST.get('password')
        print(password)

        usuario = authenticate(username=username, password=password)

        if usuario is not None:
            login(request, usuario)
            return redirect('/conta')
        else:
            messages.error(request, 'Credenciais estão incorretas!\nTente Novamente!')
            return redirect('/login')

    def get(self, request):
        print('Estou no GET')
        return redirect('/')


class CadastrarContaView(TemplateView):
    template_name = 'cadastrar.html'


class ContaView(TemplateView):
    template_name = 'conta.html'

    def get_context_data(self, **kwargs):
        context = super(ContaView, self).get_context_data(**kwargs)
        context['contas'] = Conta.objects.filter(usuario=self.request.user)
        print(context['contas'])
        print(type(context['contas']))
        return context
