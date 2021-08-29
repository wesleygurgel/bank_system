from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

import core.views as view
import core.models as model


class TestsViews(TestCase):

    def setUp(self) -> None:
        self.client = Client()
        self.login_url = reverse('login')
        self.user = {
            'email': 'teste@gmail.com',
            'username': 'username',
            'password': 'password',
            'password2': 'password',
            'name': 'fullname'
        }

    def test_index_GET(self):
        response = self.client.get(reverse('index'))

        self.assertEquals(response.status_code, 200)
        assert 'index.html' in (template.name for template in response.templates)

    def test_login_GET(self):
        response = self.client.get(self.login_url)

        self.assertEquals(response.status_code, 200)
        assert 'login.html' in (template.name for template in response.templates)

    def test_conta_GET(self):
        response = self.client.get(reverse('conta'))

        self.assertEquals(response.status_code, 302)
