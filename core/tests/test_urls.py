from django.test import SimpleTestCase
from django.urls import reverse, resolve
import core.views as views


class TestsUrl(SimpleTestCase):

    def tests_index_url_resolves(self):
        url = reverse('index')
        self.assertEquals(resolve(url).func.view_class, views.IndexView)

    def tests_login_url_resolves(self):
        url = reverse('login')
        self.assertEquals(resolve(url).func.view_class, views.LoginView)

    def tests_conta_url_resolves(self):
        url = reverse('conta')
        self.assertEquals(resolve(url).func.view_class, views.ContaView)

    def tests_conta_alterar_url_resolves(self):
        url = reverse('alterar_conta', args=['1'])
        self.assertEquals(resolve(url).func.view_class, views.AlterarContaView)

    def tests_transferir_url_resolves(self):
        url = reverse('transferir', args=['1'])
        self.assertEquals(resolve(url).func.view_class, views.TransferirView)
