# import types
# import threading


# class EventManager:
#     """
#     """

#     def __init__(self):
#         self._lock = threading.Lock()
#         self._events = {}

#     def __get_event_name(self, event):
#         return event.__name__

#     def __add_event(self, event_name, event):
#         if self.__exist_event(event_name):
#             raise Exception(f"event {event_name} Already exists")

#     def __remove_event(self, event_name):
#         if self.__exist_event(event_name):
#             del self._events[event_name]

#     def __exist_event(self, event_name):
#         return self._events.get(event_name)

#     def __get_event(self, event_name):
#         return self._events.get(event_name)

#     def register(self, event):
#         with self._lock:
#             event_name = self.__get_event_name(event)
#             if not callable(event):
#                 raise Exception(f"{event_name} not callable!")
#             self.__add_event(event_name, event)

#     def unregister(self, event):
#         """Remove a event from the service."""
#         with self._lock:
#             event_name = self.__get_event_name(event)
#             self.__remove_event(event_name)

#     def call_event(_thread, wait_for_result, event_name, *args, **kw):
#         event = self.__get_event(event_name)
#         assert event is not None
#         t = _thread.submit(event, *args, **kw)
#         if wait_for_result:
#             # 这里会一直阻塞等待结果返回
#             return t.result()
#         return t


# class ClassManager(EventManager):
#     def __get_class_functions(event):
#         return filter(lambda x: not x.startswith(
#             '_'), event.__dict__.keys())

#     def __get_event_names(event):
#         class_name = self.__get_event_name(event)
#         function_names = __get_class_functions(event)
#         return map(lambda x: f'{class_name}.x', function_names)


#     def register(self, event):
#         with self._lock:
#             if type(event) is not types.ClassType:
#                 raise Exception(f"{event_name} not callable!")

#             for event_name in self.__get_event_names(event):
#                 self.__add_event(event_name, event)

#     def unregister(self, event):
#         """Remove a event from the service."""
#         with self._lock:
#             for event_name in self.__get_event_names(event):
#                 self.__remove_event(event_name)

# if __name__ == "__main__":
#     print(list(filter(lambda x: not x.startswith('_'), EventManager.__dict__.keys())))
