import unittest
from remote_execution import app


class TestForm(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()
        app.config["WTF_CSRF_ENABLED"] = False
        self.base_url: str = 'http://127.0.0.1:5000/run_code?'

    def test_small_timeout(self):
        """Test return except"""
        body = {'code': 'python -c "print(999999999**999999999)"', 'timeout': 1}
        response = self.app.post(self.base_url, data=body)
        self.assertIn('timed out after', response.data.decode())

    def test_invalid_input(self):
        """Test return 'Invalid input except'"""
        body = {'code': 'python -c "print(999)"', 'timeout': 'Text for made except'}
        response = self.app.post(self.base_url, data=body)
        self.assertIn('Number must be between 1 and 30.', response.data.decode())

    def test_unsafe_input(self):
        """Test return 'BlockingIOError'"""
        cmd = ('prlimit --nproc=1:1 python -c "'
               'from subprocess import run'
               'run(["./kill_the_system.sh"])"')

        body = {'code': cmd, 'timeout': 3}
        response = self.app.post(self.base_url, data=body)
        print(response.data.decode())


if __name__ == '__main__':
    unittest.main()
