from game.models import Category, Page
from django.test import TestCase
from django.contrib.auth.models import User


class AdminInterfaceTests(TestCase):

    def setUp(self):
 
        User.objects.create_superuser('testAdmin', 'email@email.com', 'adminPassword123')
        self.client.login(username='testAdmin', password='adminPassword123')
        
        category = Category.objects.get_or_create(name='TestCategory')[0]
        Page.objects.get_or_create(title='TestPage1', url='https://www.google.com', category=category)
    
    def test_admin_interface_accessible(self):
        response = self.client.get('/admin/')
        self.assertEqual(response.status_code, 200)

    def test_models_present(self):

        response = self.client.get('/admin/')
        response_body = response.content.decode()

        self.assertTrue('Categories' in response_body)
        self.assertTrue('Pages' in response_body)