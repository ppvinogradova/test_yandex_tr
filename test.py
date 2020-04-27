import unittest
import requests
import json


class TranslateTest(unittest.TestCase):

    def setUp(self):
        self.API_KEY = "trnsl.1.1.20200426T121032Z.7a81dbe5256f955c.b7585959b80216b6c6086ef4beb43b744833966d"
        self.request_params = {
            'key': self.API_KEY,
            'text': 'apple',
            'lang': 'ru'
        }

    def test_trnsl_pos(self):
        get_trnsl = requests.get(
            'https://translate.yandex.net/api/v1.5/tr.json/translate',
            params=self.request_params
        )
        response = get_trnsl.json()
        result = str(response['text'][0])
        self.assertEqual(result, 'яблоко')

    def test_code_pos(self):
        get_trnsl = requests.get(
            'https://translate.yandex.net/api/v1.5/tr.json/translate',
            params=self.request_params
        )
        response = get_trnsl.json()
        result = str(response['code'])
        self.assertEqual(result, '200')

class NegTests(unittest.TestCase):

    def setUp(self):
        self.API_KEY = 'trnsl.1.1.20200426T121032Z.7a81dbe5256f955c.b7585959b80216b6c6086ef4beb43b744833966d'
        self.request_params = {
            'key': self.API_KEY,
            'text': 'apple',
            'lang': 'ru'
        }

    def test_401_error(self):
        self.API_KEY = 'rnsl.1.1.20200426T121032Z.7a81dbe5256f955c.b7585959b80216b6c6086ef4beb43b744833966d'
        self.request_params = {
            'key': self.API_KEY,
            'text': 'apple',
            'lang': 'ru'
        }
        get_trnsl = requests.get(
            'https://translate.yandex.net/api/v1.5/tr.json/translate',
            params=self.request_params
        )
        response = get_trnsl.json()
        result = str(response['code'])
        self.assertEqual(result, '401')


if __name__ == '__main__':
    unittest.main()
