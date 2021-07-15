from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView, FormView
from django.contrib.auth import authenticate, login, get_user_model
from django.urls import reverse_lazy
from .models import Conta
from .forms import CadastrarForm
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
        password = request.POST.get('password')

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


class CadastrarContaView(View):
    def get(self, request):
        if str(request.user) != 'AnonymousUser':
            User = get_user_model()
            context = {'usuarios': User.objects.all()}
            return render(request, 'cadastrar.html', context)
        else:
            return redirect('/login')


class SubmitCadastrarContaView(FormView):
    template_name = 'cadastrar.html'
    form_class = CadastrarForm
    success_url = reverse_lazy('conta')

    def form_valid(self, form, *args, **kwargs):
        form.criar_conta()
        messages.success(self.request, 'Conta cadastrada com sucesso!')
        print('Form Valid!')
        return super(SubmitCadastrarContaView, self).form_valid(form, *args, **kwargs)

    def form_invalid(self, form, *args, **kwargs):
        print('Form invalid!')
        return super(SubmitCadastrarContaView, self).form_invalid(form, *args, **kwargs)


class AlterarContaView(View):
    def get(self, request, *args, **kwargs):
        print(self.kwargs['id_conta'])
        return render(request, 'alterar_cadastro.html')


class ContaView(TemplateView):
    template_name = 'conta.html'

    def get_context_data(self, **kwargs):
        context = super(ContaView, self).get_context_data(**kwargs)
        context['contas'] = Conta.objects.filter(usuario=self.request.user).order_by('id')
        return context
