from const import CONSUMER_TYPE_EVENT
from const import CONSUMER_TYPE_EVENT_DELAY
from consumer import Consumer
from consumer import EventConsumer
from consumer import EventConsumerDelay


class BaseConsumerFactory():
    def __init__(self):
        self.consumers = dict()
        self.consumers[CONSUMER_TYPE_EVENT] = EventConsumer
        self.consumers[CONSUMER_TYPE_EVENT_DELAY] = EventConsumerDelay

    def run_consumer(self, consumer_type, *args, **kw):
        consumer = self._get_consumer(consumer_type)
        consumer(*args, **kw)

    def _get_consumer(self, consumer_type):
        consumer = self.consumers[consumer_type]
        if not issubclass(consumer, Consumer):
            raise AttributeError(f'{consumer} must be Consumer\'s instance')
        return consumer


class ConsumerFactory(BaseConsumerFactory):
    pass
