import unittest
from redirect import Redirect


class TestResirect(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.stdout_text = 'stdout text'
        cls.stderr_text = 'stderr text'

    def test_stdout_stderr(self) -> None:
        """Тест перехватывает поток вывода и ошибок, перенаправляя их в txt файлы"""
        with open('test_stdout.txt', 'w') as stdout_file, open('test_stderr.txt', 'w') as stderr_file:
            with Redirect(stdout=stdout_file, stderr=stderr_file):
                print(self.stdout_text)
                raise Exception(self.stderr_text)

        with open('test_stdout.txt', 'r') as stdout_file, open('test_stderr.txt', 'r') as stderr_file:
            stdout = stdout_file.read()
            stderr = stderr_file.read()
        self.assertIn(self.stdout_text, stdout)
        self.assertIn(self.stderr_text, stderr)

    def test_stdout_only(self) -> None:
        """Тест перехватывает и перенаправляет stdout в txt файл"""
        with open('testOnly_stdout.txt', 'w') as stdout_file:
            with Redirect(stdout=stdout_file):
                print(self.stdout_text)
        with open('testOnly_stdout.txt', 'r') as stdout_file:
            stdout = stdout_file.read()
        self.assertIn(self.stdout_text, stdout)

    def test_stderr_only(self) -> None:
        """Тест перехватывает и перенаправляет stderr в txt файл"""
        with open('testOnly_stderr.txt', 'w') as stderr_file:
            with Redirect(stderr=stderr_file):
                raise Exception(self.stderr_text)
        with open('testOnly_stderr.txt', 'r') as stderr_file:
            stderr = stderr_file.read()
        self.assertIn(self.stderr_text, stderr)

    def test_stderr_stdout_turn_off(self) -> None:
        """Тест не перехватывает потоки. Выводы txt будут пустыми."""
        with self.assertRaises(Exception):
            with open('stdout.txt', 'w') as file_out, open('stderr.txt', 'w') as file_err:
                with Redirect():
                    print(self.stdout_text)
                    raise Exception(self.stderr_text)
        with open('stdout.txt', 'r') as file_out, open('stderr.txt', 'r') as file_err:
            stdout, stderr = file_out.read(), file_err.read()
        self.assertFalse(self.stderr_text in stderr)
        self.assertFalse(self.stdout_text in stdout)


if __name__ == '__main__':
    unittest.main()
    # with open('test_results.txt', 'a') as test_file_stream:
    #     runner = unittest.TextTestRunner(stream=test_file_stream)
    #     unittest.main(testRunner=runner)
