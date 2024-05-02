import unittest
import time
from module_03_ci_culture_beginning.homework.hw3.accounting import app


class TestMaxNumberApp(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        cls.app = app.test_client()
        cls.add_url: str = '/add/'
        cls.calculate_url: str = '/calculate'
        cls.dates: tuple = ('20000311', '20000312', '20010513', '20010514')
        cls.expenses: tuple = ('100', '200', '300', '400')

    def test_filling_storage(self):
        """Функция заполнения storage"""
        for index in range(3):
            response = self.app.get(self.add_url + self.dates[index] + '/' + self.expenses[index])
            with self.subTest(response.data.decode()):
                self.assertIn('добавлена', response.data.decode())

    def test_get_calculate_year(self):
        """Функция проверки endpoint /calculate/<int:year>"""
        self.test_filling_storage()
        for date in self.dates:
            response = self.app.get(self.calculate_url + '/' + date[:4])
            response = response.data.decode()
            with self.subTest(response):
                self.assertTrue(float(response) > 0)

    def test_get_calculate_year_month(self):
        """Функция проверки endpoint /calculate/<int:year>/<int:month>"""
        self.test_filling_storage()
        for date in self.dates:
            response = self.app.get(self.calculate_url + '/' + date[:4] + '/' + date[4:6])
            response = response.data.decode()
            with self.subTest(response):
                self.assertTrue(float(response) > 0)

    def test_add_invalid_date(self):
        """Проверка не корректной даты"""
        response = self.app.get(self.add_url + '230506/100')
        response = response.data.decode()
        with self.assertRaises(ValueError):
            time.strptime(response[8:14], '%y%m%d')

    def test_calculate_from_empty_storage(self):
        """Проверка вывода суммы расходов при пустой storage"""
        response = self.app.get(self.calculate_url + '20201204/222')
        response = response.data.decode()
        with self.assertRaises(ValueError):
            self.assertTrue(int(response) > 0)
