from engine import Engine
from job import JobSleep, JobPrint


def main():
    engine = Engine()

    engine.register('JobSleep', JobSleep)
    engine.register('JobPrint', JobPrint)

    engine.send_message('JobSleep')
    engine.send_message('JobSleep')
    engine.send_message('JobPrint')
    engine.send_message('JobPrint')
    engine.send_message('JobPrint')
    engine.send_message('JobSleep')


if __name__ == '__main__':
    main()
