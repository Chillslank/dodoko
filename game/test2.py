from game.models import Category, Page
from django.test import TestCase



class ModelTests(TestCase):

    def setUp(self):
        category_py = Category.objects.get_or_create(name='Action', views=123, likes=55)
        Category.objects.get_or_create(name='FPS', views=187, likes=90)
        
        Page.objects.get_or_create(category=category_py[0],
                                   title='PUBG',
                                   url='https://store.steampowered.com/app/578080/PUBG_BATTLEGROUNDS/',
                                   views=156)
    
    def test_category_model(self):

        category_py = Category.objects.get(name='Action')
        self.assertEqual(category_py.views, 123)
        self.assertEqual(category_py.likes, 55)
        
        category_dj = Category.objects.get(name='FPS')
        self.assertEqual(category_dj.views, 187)
        self.assertEqual(category_dj.likes, 90)
    
    def test_page_model(self):

        category_py = Category.objects.get(name='Action')
        page = Page.objects.get(title='PUBG')
        self.assertEqual(page.url, 'https://store.steampowered.com/app/578080/PUBG_BATTLEGROUNDS/')
        self.assertEqual(page.views, 156)
        self.assertEqual(page.title, 'PUBG')
        self.assertEqual(page.category, category_py)