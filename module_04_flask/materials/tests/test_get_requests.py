import unittest

from module_04_flask.materials.get_requests import app


class TestMaxNumberApp(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()

    def test_search(self):
        url_for_test = '/search/?cell_tower_id=1&date_from=20001011&date_to=20011210&phone_prefix=999*&protocol=4G'
        request = self.app.get(url_for_test)
        print(request.data.decode())

    def test_search_dont_can_get_invalid_dates(self):
        url_for_test = '/search/?cell_tower_id=1&date_from=20001011&date_to=99999999&phone_prefix=999*&protocol=4G'
        request = self.app.get(url_for_test)
        self.assertTrue(request.status_code, 400)

    def test_search_dont_can_get_invalid_phone(self):
        url_for_test = '/search/?cell_tower_id=1&date_from=20001011&date_to=20011210&phone_prefix=99999999999999&protocol=4G'
        request = self.app.get(url_for_test)
        self.assertTrue(request.status_code, 400)

    def test_search_dont_can_get_invalid_tower_ids(self):
        url_for_test = '/search/?cell_tower_id=0&date_from=20001011&date_to=20011210&phone_prefix=999*&protocol=4G'
        request = self.app.get(url_for_test)
        self.assertTrue(request.status_code, 400)

    def test_search_dont_can_get_invalid_protocols(self):
        url_for_test = '/search/?cell_tower_id=1&date_from=20001011&date_to=20011210&phone_prefix=999*&protocol=8G'
        request = self.app.get(url_for_test)
        self.assertTrue(request.status_code, 400)

    def test_list_nums_return_correct_results(self):
        request = self.app.get('/sum-prod/?numbers=1&numbers=2&numbers=3')
        request = request.data.decode()
        self.assertEqual(request, '6, 6')

    def test_valid_combinations(self):
        request = self.app.get('/combinations/?number_1=1&number_1=2&number_1=3&&number_2=4&&number_2=5&&number_2=6&')
        request = request.data.decode()
        true_string = '[(1, 4), (1, 5), (1, 6), (2, 4), (2, 5), (2, 6), (3, 4), (3, 5), (3, 6)]'
        self.assertEqual(request, true_string)

    def test_similar(self):
        request = self.app.get('/similar/?numbers=1&numbers=2&numbers=22&numbers=23&dad=3')
        request = request.data.decode()
        self.assertEqual(request, '2')
