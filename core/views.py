from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView, FormView
from django.contrib.auth import authenticate, login


# Create your views here.

class IndexView(TemplateView):
    template_name = 'index.html'


class LoginView(TemplateView):
    template_name = 'login.html'


class SubmitLoginView(View):
    def post(self, request):
        username = request.POST.get('username')
        print(username)
        password = request.POST.get('password')
        print(password)

        usuario = authenticate(username=username, password=password)

        if usuario is not None:
            login(request, usuario)
            return redirect('/')

    def get(self, request):
        print('Estou no GET')
        redirect('/')


class ContaView(TemplateView):
    template_name = 'conta.html'
