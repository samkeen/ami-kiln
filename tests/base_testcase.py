import unittest
from os import path


class BaseTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.top_dir = path.abspath(path.dirname(__file__))
        cls.fixture_dir = path.join(cls.top_dir, 'fixtures')
        super().setUpClass()
