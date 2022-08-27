import unittest
from YandexApi import createfolder, get_folder_info

FOLLDERNAME = 'test'


class TesYandexApi(unittest.TestCase):
    def test_createfolder(self):
        result = createfolder(FOLLDERNAME)
        self.assertTrue(result == 201, f'Сервер ответил: {result}')
    def test_get_folder_info(self):
        self.assertTrue(get_folder_info(FOLLDERNAME) == 'dir')
