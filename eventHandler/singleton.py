import threading


class Singleton(object):
    _instance_lock = threading.Lock()
    _instance_init = False

    def __init__(self, *args, **kwargs):
        with self._instance_lock:
            if not self._instance_init:
                self._instance_init = True
                return

    def __new__(cls, *args, **kwargs):
        with cls._instance_lock:
            if not hasattr(cls, '_instance'):
                cls._instance = super().__new__(cls)
            return cls._instance


if __name__ == "__main__":
    s1 = Singleton()
    s2 = Singleton()
    print('s1', s1)
    print('s2', s2)
