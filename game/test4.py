import os
from django.test import TestCase
from django.conf import settings

class Chapter4StaticMediaTests(TestCase):

    def setUp(self):
        self.project_base_dir = os.getcwd()
        self.static_dir = os.path.join(self.project_base_dir, 'static')
        self.media_dir = os.path.join(self.project_base_dir, 'media')
    
    def test_does_static_directory_exist(self):

        does_static_dir_exist = os.path.isdir(self.static_dir)
        does_images_static_dir_exist = os.path.isdir(os.path.join(self.static_dir, 'images'))
        does_logo_jpg_exist = os.path.isfile(os.path.join(self.static_dir, 'images', 'logo.png'))
        
        self.assertTrue(does_static_dir_exist)
        self.assertTrue(does_images_static_dir_exist)
        self.assertTrue(does_logo_jpg_exist)

    
    def test_static_configuration(self):
 
        static_dir_exists = 'STATIC_DIR' in dir(settings)
        self.assertTrue(static_dir_exists)
        
        expected_path = os.path.normpath(self.static_dir)
        static_path = os.path.normpath(settings.STATIC_DIR)
        self.assertEqual(expected_path, static_path)
        
        staticfiles_dirs_exists = 'STATICFILES_DIRS' in dir(settings)
        self.assertTrue(staticfiles_dirs_exists)
        self.assertEqual([static_path], settings.STATICFILES_DIRS)
        
        staticfiles_dirs_exists = 'STATIC_URL' in dir(settings)
        self.assertTrue(staticfiles_dirs_exists)
        self.assertEqual('/static/', settings.STATIC_URL)

    
    def test_context_processor_addition(self):

        context_processors_list = settings.TEMPLATES[0]['OPTIONS']['context_processors']
        self.assertTrue('django.template.context_processors.debug' in context_processors_list)
        self.assertTrue('django.template.context_processors.request' in context_processors_list)
        self.assertTrue('django.contrib.auth.context_processors.auth' in context_processors_list)
        self.assertTrue('django.contrib.messages.context_processors.messages' in context_processors_list)