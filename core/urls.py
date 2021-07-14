from django.urls import path
from .views import IndexView, ContaView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('conta/', ContaView.as_view(), name='conta'),
]