import unittest

from os import path

from amiorganizer.app_config import AppConfig
from tests.base_testcase import BaseTestCase


class TestAppConfig(BaseTestCase):
    """
    Simple initial test in order to try testing frameworks such as Tox
    """
    def test_proof_of_life(self):
        app_config = AppConfig(path.join(self.fixture_dir, 'config.yml'))
        self.assertEqual('debug', app_config.app_config['appConfig']['logLevel'])
