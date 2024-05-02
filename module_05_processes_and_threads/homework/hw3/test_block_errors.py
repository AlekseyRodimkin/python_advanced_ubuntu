import unittest
from block_errors import BlockErrors


class TestForm(unittest.TestCase):
    def test_exc_ignored(self) -> None:
        err_types = {ZeroDivisionError, TypeError}
        with BlockErrors(err_types):
            a = 1 / 0

    def test_get_exc(self) -> None:
        with self.assertRaises(TypeError):
            err_types = {ZeroDivisionError}
            with BlockErrors(err_types):
                a = 1 / '0'

    def test_exc_in_subblock(self) -> None:
        try:
            outer_err_types = {TypeError}
            with BlockErrors(outer_err_types) as result:
                inner_err_types = {ZeroDivisionError}
                with BlockErrors(inner_err_types):
                    a = 1 / '0'
        except:
            self.fail()

    def test_ignored_sub_exc(self):
        with self.assertRaises(Exception):
            with BlockErrors({}):
                a = 1 / '0'


if __name__ == '__main__':
    unittest.main()
