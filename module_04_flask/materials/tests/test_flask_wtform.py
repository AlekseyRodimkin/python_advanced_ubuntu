import unittest

from module_04_flask.materials.flask_wtform import app


class TestForm(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        cls.app = app.test_client()
        app.config["WTF_CSRF_ENABLED"] = False
        cls.base_url: str = 'http://127.0.0.1:5000/'
        cls.body: dict = {'name': 'Ivan', 'surname': 'Ivanov',
                          'phone': 1234567890, 'address': 'Moscow', 'email': 'IVAN@example.com'}

    def test_400_without_name(self):
        self.body.pop('name')
        response = self.app.post(self.base_url + 'registration?', data=self.body)
        self.assertIn('name', response.data.decode())
        self.assertEqual(response.status_code, 400)

    def test_400_without_surname(self):
        self.body.pop('surname')
        response = self.app.post(self.base_url + 'registration?', data=self.body)
        self.assertIn('surname', response.data.decode())
        self.assertEqual(response.status_code, 400)

    def test_400_without_phone(self):
        self.body.pop('phone')
        response = self.app.post(self.base_url + 'registration?', data=self.body)
        self.assertIn('phone', response.data.decode())
        self.assertEqual(response.status_code, 400)

    def test_400_without_address(self):
        self.body.pop('address')
        response = self.app.post(self.base_url + 'registration?', data=self.body)
        self.assertIn('address', response.data.decode())
        self.assertEqual(response.status_code, 400)

    def test_400_without_email(self):
        self.body.pop('email')
        response = self.app.post(self.base_url + 'registration?', data=self.body)
        self.assertIn('email', response.data.decode())
        self.assertEqual(response.status_code, 400)

    def test_400_invalid_len_phone(self):
        self.body['phone'] = '2345'
        response = self.app.post(self.base_url + 'registration?', data=self.body)
        self.assertIn('phone', response.data.decode())
        self.assertEqual(response.status_code, 400)

    def test_lucky_ticket(self):
        self.body: dict = {'name': 'Ivan', 'family_name': 'Plato', 'ticket_number': 132060}
        response = self.app.post(self.base_url + 'luckyticket?', data=self.body)
        self.assertIn(self.body['name'], response.data.decode())
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
