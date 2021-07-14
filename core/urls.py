from django.urls import path
from .views import IndexView, LoginView, ContaView, SubmitLoginView
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('login/', LoginView.as_view(), name='login'),
    path('login/submit', SubmitLoginView.as_view(), name='login_submit'),
    path('conta/', login_required(ContaView.as_view(), login_url='login'), name='conta'),
]