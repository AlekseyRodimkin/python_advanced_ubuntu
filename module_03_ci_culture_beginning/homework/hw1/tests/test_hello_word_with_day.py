import unittest
from freezegun import freeze_time
from module_03_ci_culture_beginning.materials.previous_hw_test.hello_word_with_day import app


class TestMaxNumberApp(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        cls.app = app.test_client()
        cls.base_url = '/hello-world/'
        cls.username = 'username'

    def test_can_get_correct_username_with_weekdate(self):
        response = self.app.get(self.base_url + self.username)
        response_text = response.data.decode()
        self.assertTrue(self.username in response_text)

    @freeze_time("2023-12-04")
    def test_date_1(self):
        response = self.app.get(self.base_url + self.username)
        response_text = response.data.decode()
        self.assertTrue('понедельника' in response_text)

    @freeze_time("2023-12-05")
    def test_date_2(self):
        response = self.app.get(self.base_url + self.username)
        response_text = response.data.decode()
        self.assertTrue('вторника' in response_text)

    @freeze_time("2023-12-06")
    def test_date_3(self):
        response = self.app.get(self.base_url + self.username)
        response_text = response.data.decode()
        self.assertTrue('среды' in response_text)

    @freeze_time("2023-12-07")
    def test_date_4(self):
        response = self.app.get(self.base_url + self.username)
        response_text = response.data.decode()
        self.assertTrue('четверга' in response_text)

    @freeze_time("2023-12-08")
    def test_date_5(self):
        response = self.app.get(self.base_url + self.username)
        response_text = response.data.decode()
        self.assertTrue('пятницы' in response_text)

    @freeze_time("2023-12-09")
    def test_date_6(self):
        response = self.app.get(self.base_url + self.username)
        response_text = response.data.decode()
        self.assertTrue('субботы' in response_text)

    @freeze_time("2023-12-10")
    def test_date_7(self):
        response = self.app.get(self.base_url + self.username)
        response_text = response.data.decode()
        self.assertTrue('воскресенья' in response_text)