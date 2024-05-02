import unittest

from module_03_ci_culture_beginning.homework.hw4.person import Person


class TestSocialAge(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.man = Person(name='Ivan', year_of_birth=2000, address='Boston')

    def test_get_age(self):
        """Проверка получения возраста"""
        self.assertTrue(self.man.get_age() > 0, 'Returned low age.')

    def test_get_name(self):
        """Проверка получения имени"""
        self.assertEqual(self.man.get_name(), self.man.name, 'Returned invalid name')

    def test_set_name(self):
        """Проверка изменения имени"""
        new_name = 'Not_Ivan'
        self.man.set_name(new_name)
        self.assertEqual(self.man.get_name(), new_name, 'Name has not been changed.')

    def test_set_address(self):
        """Проверка изменения адреса"""
        new_address = 'Not_Boston'
        self.man.set_address(new_address)
        self.assertEqual(self.man.get_address(), new_address, 'Address has not been changed.')

    def test_is_homeless(self):
        self.assertEqual(type(self.man.is_homeless()), bool, 'Returned not bool')
