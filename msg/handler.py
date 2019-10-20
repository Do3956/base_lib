import abc
import time


class BaseHandler(metaclass=abc.ABCMeta):
    """事件基类"""

    def __init__(self, delay=0):
        if not isinstance(delay, (int, float)) or delay < 0.0:
            raise AttributeError('delay error, must be gte 0.0')
        self.delay = delay

    @abc.abstractmethod
    def execute(self, *args, **kwargs):
        """执行"""
        pass


class ReaderHandler(BaseHandler):

    def __read_book(self, *args, **kwargs):
        book_name = kwargs.get('book_name')
        if not book_name:
            return
        print(f"{time.time()}, 正在看书:<<{book_name}>>")

    def execute(self, *args, **kwargs):
        self.__read_book(*args, **kwargs)

    def callback(self, *args, **kwargs):
        print(f'{time.time()}, ReaderHandler.callback, args:{args}, kwargs:{kwargs}')


class AuthorHandler(BaseHandler):

    def __write_book(self, *args, **kwargs):
        book_name = kwargs.get('book_name')
        if not book_name:
            return
        print(f'{time.time()}, <<{book_name}>>书籍出版')

    def execute(self, *args, **kwargs):
        self.__write_book(*args, **kwargs)

    def callback(self, *args, **kwargs):
        print(f'{time.time()}, AuthorHandler.callback, args:{args}, kwargs:{kwargs}')


class SleepHandler(BaseHandler):

    def __sleep(self, *args, **kwargs):
        second = kwargs.get('second')
        if not isinstance(second, (int, float)) or second <= 0.0:
            return
        time.sleep(second)
        print(f"{time.time()}, 休息{second}秒")

    def execute(self, *args, **kwargs):
        self.__sleep(*args, **kwargs)


if __name__ == "__main__":
    print(issubclass(BaseHandler, AuthorHandler))
    print(issubclass(AuthorHandler, BaseHandler))
    print(issubclass(AuthorHandler().__class__, BaseHandler))
