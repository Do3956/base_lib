"""
单例模式
定义: 一个类只能生成一个实例
场景:
    1. 日志记录
    2. 数据库操作
    3. 打印机等后台程序
创建方法:
    1. 将构造函数私有化
    2. 创建静态类来完成对象的初始化, 此时一个类仅返回一个实例
    PS: python中无法将构造函数私有化
Python中创建方法:
    1. 重写 __new__, 存在则不创建实例
    2. 懒式加载, 比如操作数据库的对象
    3. 模块级别均是单例模式: 模块导入时候, 会被初始化; 统一模块再次导入时候, 就不会再次初始化.
    4. 单态模式的单例: 所有对象共享相同的状态, Python中用__dict__存储一个类所有对象的状态, 基于__init__或者__new__都可以
    5. 基于元类的单例
    6. 装饰器单例
单例的缺点(相当于有全局访问权限):
    1. 全局变量已经修改, 但是开发人员无感知, 且该变量按照开发人员以为的值去使用
    2. 会对一个对象创建多个引用, 其中一个引用未结束, 内存不能释放
"""
import threading


def synchronized(func):
    func.__lock__ = threading.Lock()

    def lock_func(*args, **kwargs):
        with func.__lock__:
            return func(*args, **kwargs)
    return lock_func


class Singleton:
    """单例类"""
    has_init = False

    # @synchronized
    def __init__(self, *args, **kwargs):
        if not self.has_init:
            self.has_init = True
            print(1111)
            return
        print(222)

    @synchronized
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance


class LazySingleton:
    """懒式单例类"""
    __instance = None

    def __init__(self):
        if not self.__class__.__instance:
            print("__init__ method called")
        else:
            print(f"instance already created: {self.get_instance()}")

    @classmethod
    @synchronized
    def get_instance(cls):
        if not cls.__instance:
            cls.__instance = Singleton()
        return cls.__instance


class MonostateSingleton:
    """单态单例"""
    __share_state = {'status': 'normal'}

    def __init__(self):
        self.diff = 0
        self.__dict__ = self.__share_state


class MetaSingleton:
    """元类单例"""

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

def singleton(cls, *args, **kw):
    """单例装饰器"""
    instance = {}

    def _singleton():
        if cls not in instance:
            instance[cls] = cls(*args, **kw)
        return instance[cls]
    return _singleton


if __name__ == '__main__':
    # s1 = Singleton()
    # s2 = Singleton()
    # print(f"{type(s1)} {type(s2)}")
    # print(f"{s1} {s2}")
    # print(f"s1: {id(s1)}, s2: {id(s2)}, s1 <-{s1 is s2}-> s2")
    ls1 = LazySingleton.get_instance()
    ls2 = LazySingleton.get_instance()
    print(f"ls1: {id(ls1)}, ls2: {id(ls2)}, ls1 <-{ls1 == ls2}-> ls2")
    # ms1 = MonostateSingleton()
    # ms2 = MonostateSingleton()
    # ms2.dff = 1
    # print(f"ms1.__dict__: {ms1.__dict__}, ms2.__dict__: {ms2.__dict__}")
