import os
from django.test import TestCase
from django.conf import settings

class ProjectStructureTests(TestCase):
    def setUp(self):
        self.project_base_dir = os.getcwd()
        self.game_app_dir = os.path.join(self.project_base_dir, 'game')
    
    
    def test_project_created(self):
        directory_exists = os.path.isdir(os.path.join(self.project_base_dir, 'dodoko'))
        urls_module_exists = os.path.isfile(os.path.join(self.project_base_dir, 'dodoko', 'urls.py'))
        
        self.assertTrue(directory_exists)
        self.assertTrue(urls_module_exists)
    
    def test_game_app_created(self):

        directory_exists = os.path.isdir(self.game_app_dir)
        is_python_package = os.path.isfile(os.path.join(self.game_app_dir, '__init__.py'))
        views_module_exists = os.path.isfile(os.path.join(self.game_app_dir, 'views.py'))
        
        self.assertTrue(directory_exists)
        self.assertTrue(is_python_package)
        self.assertTrue(views_module_exists)
    
    def test_game_has_urls_module(self):
        
        module_exists = os.path.isfile(os.path.join(self.game_app_dir, 'urls.py'))
        self.assertTrue(module_exists)
    
    def test_is_game_app_configured(self):

        is_app_configured = 'game' in settings.INSTALLED_APPS
        
        self.assertTrue(is_app_configured)