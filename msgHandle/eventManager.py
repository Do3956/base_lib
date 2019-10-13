import types
import threading
from singleton import Singleton
from threadPool import thread_pool


class EventManager(Singleton):
    """
    """

    def __init__(self):
        self._lock = threading.Lock()
        self._events = {}

    def _get_event_name(self, event):
        return event.__name__

    def _add_event(self, event_name, event):
        if self._exist_event(event_name):
            raise Exception(f"event {event_name} Already exists")
        self._events[event_name] = event

    def _remove_event(self, event_name):
        if self._exist_event(event_name):
            del self._events[event_name]

    def _exist_event(self, event_name):
        return self._events.get(event_name)

    def _get_event(self, event_name):
        return self._events.get(event_name)

    def register(self, event):
        with self._lock:
            event_name = self._get_event_name(event)
            if not callable(event):
                raise Exception(f"{event_name} not callable!")
            self._add_event(event_name, event)

    def unregister(self, event):
        """Remove a event from the service."""
        with self._lock:
            event_name = self._get_event_name(event)
            self._remove_event(event_name)

    def call_event(self, wait_for_result, _, event_name, *args, **kw):
        event = self._get_event(event_name)
        assert event is not None
        t = thread_pool.workers.submit(event, *args, **kw)
        if wait_for_result:
            # 这里会一直阻塞等待结果返回
            return t.result()
        return t


class ClassEventManager(EventManager):
    def _get_class_functions(self, event):
        return list(filter(lambda x: not x.startswith(
            '_'), event.__dict__.keys()))

    def _get_event_names(self, event):
        class_name = self._get_event_name(event)
        function_names = self._get_class_functions(event)
        return map(lambda x: f'{class_name}.{x}', function_names)

    def register(self, event):
        with self._lock:
            if not callable(event):
                raise Exception(f"{event_name} not callable!")

            for event_name in self._get_event_names(event):
                self._add_event(event_name, event)

    def unregister(self, event):
        """Remove a event from the service."""
        with self._lock:
            for event_name in self._get_event_names(event):
                self._remove_event(event_name)

    def call_event(self, wait_for_result, _, event_name, *args, **kw):
        if _:
            event = getattr(_, event_name)
        else:
            event = self._get_event(event_name)
        assert event is not None
        t = thread_pool.workers.submit(event, *args, **kw)
        if wait_for_result:
            # 这里会一直阻塞等待结果返回
            return t.result()
        return t

def register(event_manager):
    """
    """
    def deco(cls):
        event_manager().register(cls)
        return cls
    return deco


if __name__ == "__main__":
    print(list(filter(lambda x: not x.startswith('_'), EventManager._dict_.keys())))
    print('ClassEventManager', ClassEventManager())
