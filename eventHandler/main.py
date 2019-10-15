from engine import Engine
from threadPool import thread_pool
from coroutinePool import coroutine_pool


def run_by_thread():
    from job import JobSleep, JobPrint

    engine = Engine(thread_pool.workers)

    engine.register('JobSleep', JobSleep)
    engine.register('JobPrint', JobPrint)

    engine.send_message('JobSleep')
    engine.send_message('JobSleep')
    engine.send_message('JobSleep')
    engine.send_message('JobPrint')
    engine.send_message('JobPrint')
    engine.send_message('JobPrint')
    engine.send_message('JobSleep')
    engine.send_message('JobSleep')


def run_by_coroutine():
    """
    todo 协程版本：目前还没调通，有些问题
    """
    from coroutineJob import JobSleep, JobPrint

    print(11111)
    engine = Engine(coroutine_pool)
    engine.register('JobSleep', JobSleep)
    engine.register('JobPrint', JobPrint)

    print(22222)
    engine.send_message('JobSleep')
    engine.send_message('JobSleep')
    engine.send_message('JobSleep')
    engine.send_message('JobPrint')
    engine.send_message('JobPrint')
    engine.send_message('JobPrint')
    engine.send_message('JobSleep')
    engine.send_message('JobSleep')
    print(3333)

def main():
    run_by_thread()
    # run_by_coroutine()


if __name__ == '__main__':
    main()
