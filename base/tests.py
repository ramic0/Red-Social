from django.test import TestCase
from .models import Perfil

# Create your tests here.

#class AuthorListViewTest(TestCase):
#    def test_view_url_exists_at_desired_location(self):
#        resp = self.client.get('/perfiles/')
#        self.assertEqual(resp.status_code, 200)

class PerfilTestCase(TestCase):
    def setUp(self):
        Perfil.objects.create(name="jefferson", email="jeff@gamil.com", bio="software")

    def lenght(self):
       post = Perfil.objects.get(name='jefferson').post_set-all()[0]
       max_length = post._meta.get_field('content').max_length
       self.assertEquals(max_length,600)

    