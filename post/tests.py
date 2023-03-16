from django.contrib.auth.models import User
from django.test import RequestFactory, TestCase
from .views import ver_post

class SimpleTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='jef', email='jef@jeg.com', password='123')

    def test_details(self):
        request = self.factory.get('/ver/')
        request.user = self.user
        response = ver_post(request)
        self.assertEqual(response.status_code, 200)

        