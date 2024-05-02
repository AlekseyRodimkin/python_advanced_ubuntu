import unittest
import os

from module_03_ci_culture_beginning.materials.head_file_test.head_file import app


class TestHeadFile(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()
        self.base_url = '/headfile/'

    def test_make_new_file(self):
        filename = 'filename.txt'
        response = self.app.get(self.base_url + filename)
        response_text = response.data.decode()
        self.assertTrue(filename in response_text)

    def tearDown(self):
        os.remove('filename.txt')
        with self.assertRaises(FileNotFoundError):
            with open('filename.txt', 'r') as f:
                pass
