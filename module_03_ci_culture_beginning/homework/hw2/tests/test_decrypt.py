import unittest
from module_03_ci_culture_beginning.homework.hw2.decrypt import decrypt


class TestMaxNumberApp(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data: dict = {'абра-кадабра': ['абра-кадабра.', 'абраа..-кадабра', 'абраа..-.кадабра',
                                           'абра--..кадабра', 'абрау...-кадабра', ],

                          '': ['абра........', '.', '1.......................'],

                          '23': ['1..2.3'],

                          'a': ['абр......a.']
                          }

    def test_uncrypt(self):
        for key, value in self.data.items():
            for string in value:
                with self.subTest(string != key):
                    self.assertEqual(key, decrypt(string))
                    