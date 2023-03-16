from django.test import TestCase

from django.test import TestCase

class LoginTestCase(TestCase):
    def test_login(self):
        response = self.client.get('/crear/post/')
        self.assertRedirects(response, '/accounts/login/?next=/crear/post/')
        with self.settings(LOGIN_URL='/accounts/login/'):
            response = self.client.get('/crear/post/')
            self.assertRedirects(response, '/accounts/login/?next=/crear/post/')
   
    