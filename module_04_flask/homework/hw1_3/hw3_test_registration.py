"""
Для каждого поля и валидатора в эндпоинте /registration напишите юнит-тест,
который проверит корректность работы валидатора. Таким образом, нужно проверить, что существуют наборы данных,
которые проходят валидацию, и такие, которые валидацию не проходят.
"""

import unittest
from hw1_registration import app


class TestForm(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        cls.app = app.test_client()
        app.config["WTF_CSRF_ENABLED"] = False
        cls.base_url: str = 'http://127.0.0.1:5000/registration?'
        cls.body: dict = {'name': 'Ivan', 'phone': 1234567890, 'address': 'Moscow',
                          'email': 'IVAN@example.com', 'index': 00000}

    def test_200(self):
        response = self.app.post(self.base_url, data=self.body)
        self.assertEqual(response.status_code, 200)

    def test_400_without_name(self):
        self.body.pop('name')
        response = self.app.post(self.base_url, data=self.body)
        self.assertIn('name', response.data.decode())
        self.assertEqual(response.status_code, 400)

    def test_400_invalid_phone(self):
        self.body['phone'] = 123
        response = self.app.post(self.base_url, data=self.body)
        self.assertIn('phone', response.data.decode())
        self.assertEqual(response.status_code, 400)

    def test_400_without_address(self):
        self.body.pop('address')
        response = self.app.post(self.base_url, data=self.body)
        self.assertIn('address', response.data.decode())
        self.assertEqual(response.status_code, 400)

    def test_400_invalid_email(self):
        self.body['email'] = 'mail.com'
        response = self.app.post(self.base_url, data=self.body)
        self.assertIn('email', response.data.decode())
        self.assertEqual(response.status_code, 400)

    def test_400_without_email(self):
        self.body.pop('email')
        response = self.app.post(self.base_url, data=self.body)
        self.assertIn('email', response.data.decode())
        self.assertEqual(response.status_code, 400)

    def test_400_without_index(self):
        self.body.pop('index')
        response = self.app.post(self.base_url, data=self.body)
        self.assertIn('index', response.data.decode())
        self.assertEqual(response.status_code, 400)

    def test_400_invalid_index(self):
        self.body['index'] = 'INDEX'
        response = self.app.post(self.base_url, data=self.body)
        self.assertIn('index', response.data.decode())
        self.assertEqual(response.status_code, 400)


if __name__ == '__main__':
    unittest.main()
