# -*- coding: utf-8 -*-
import unittest
import os
import sys

TESTS_DIR = os.path.dirname(os.path.abspath(__file__))
TEST_DATA_DIR = os.path.join(TESTS_DIR , 'data')


class YandexXmlParserTests(unittest.TestCase):

    def setUp(self):
        pass

    def get_data(self, path):
        u'возвращает содержимое любого файла по указанному пути относительно директории data'

        return open(os.path.join(TEST_DATA_DIR, path), 'r').read()

if __name__ == '__main__':
    suite = unittest.TestLoader().discover(TESTS_DIR)
    unittest.TextTestRunner(verbosity=2).run(suite)
