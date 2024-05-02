import unittest

from module_03_ci_culture_beginning.materials.testing_age.social_age import get_social_status


class TestSocialAge(unittest.TestCase):
    def test_can_get_child_age(self):
        age = 8
        expected_res = 'ребенок'
        function_res = get_social_status(age)
        self.assertEqual(expected_res, function_res)

    def test_cannot_pass_str_as_age(self):
        age = 'old'
        with self.assertRaises(ValueError):
            get_social_status(age)

    def test_cannot_pass_Bool_as_age(self):
        age = None
        with self.assertRaises(ValueError):
            get_social_status(age)