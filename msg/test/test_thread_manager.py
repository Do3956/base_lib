import unittest
from unittest import mock

from msg.thread_manager import ThreadManager


class TestThreadManager(unittest.TestCase):

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()
        # self.engine.

    def test_init(self):
        try:
            ThreadManager('fds')
        except AttributeError:
            pass

        try:
            ThreadManager(0.8)
        except AttributeError:
            pass

        try:
            ThreadManager(-8)
        except AttributeError:
            pass

        try:
            ThreadManager(0)
        except AttributeError:
            pass

        ThreadManager(8)
