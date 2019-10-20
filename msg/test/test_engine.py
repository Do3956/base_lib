import unittest
from unittest import mock

from msg.engine import EventEngine
from msg.handler import ReaderHandler


class TestEventEngine(unittest.TestCase):

    def setUp(self):
        super().setUp()
        self.engine = EventEngine()

    def tearDown(self):
        super().tearDown()
        # self.engine.

    def test_register(self):
        try:
            self.engine.register('event')
        except Exception as e:
            assert e.__str__() == '__add_handlers without handlers'

        try:
            self.engine.register('event', 78)
        except AttributeError as e:
            assert e.__str__() == '78 is not from BaseHandler'

        self.engine.register('event', ReaderHandler(), ReaderHandler())

        try:
            self.engine.register('event', ReaderHandler())
        except Exception as e:
            assert e.__str__() == 'event_name:event exist'

    def test_send(self):
        self.engine.send('event')
        try:
            self.engine.send('no_event')
        except KeyError:
            pass
