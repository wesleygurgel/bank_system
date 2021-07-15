from django.urls import path
from .views import IndexView, LoginView, ContaView, SubmitLoginView, CadastrarContaView, SubmitCadastrarContaView,\
    AlterarContaView
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('login/', LoginView.as_view(), name='login'),
    path('login/submit', SubmitLoginView.as_view(), name='login_submit'),
    path('conta/', login_required(ContaView.as_view(), login_url='login'), name='conta'),
    path('conta/cadastrar', login_required(CadastrarContaView.as_view(), login_url='login'), name='cadastrar'),
    path('conta/cadastrar/submit', SubmitCadastrarContaView.as_view(), name='cadastrar_submit'),
    path('conta/alterar/<int:id_conta>/', AlterarContaView.as_view(), name='alterar_conta'),
]