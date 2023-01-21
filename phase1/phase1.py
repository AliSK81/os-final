from multiprocessing import Process, Value
from time import sleep

from Semaphore import Locker


def add(num, value, locker):
    tmp = 0
    while True:
        locker.lock(0)
        print('add')
        num.value += value
        tmp = num.value
        sleep(1)
        if tmp != num.value:
            print("Process conflict")
        locker.unlock(0)


def sub(num, value, locker):
    tmp = 0
    while True:
        locker.lock(1)
        print('sub')
        num.value -= value
        tmp = num.value
        sleep(1.5)
        if tmp != num.value:
            print("Process conflict")
        locker.unlock(1)


def mul(num, value, locker):
    tmp = 0
    while True:
        locker.lock(2)
        print('mul')
        num.value *= value
        tmp = num.value
        sleep(2)
        if tmp != num.value:
            print("Process conflict")
        locker.unlock(2)


def div(num, value, locker):
    tmp = 0
    while True:
        locker.lock(3)
        print('div')
        num.value /= value
        tmp = num.value
        sleep(3)
        if tmp != num.value:
            print("Process conflict")
        locker.unlock(3)


def Show(num):
    while True:
        sleep(0.5)
        print(num.value)


if __name__ == '__main__':
    num = Value('d', 0.0)

    locker = Locker(4)

    p1 = Process(target=add, args=(num, 10, locker))
    p2 = Process(target=sub, args=(num, 5, locker))
    p3 = Process(target=mul, args=(num, 2, locker))
    p4 = Process(target=div, args=(num, 4, locker))

    show = Process(target=Show, args=(num,))
    show.start()
    sleep(1)
    p1.start()
    p2.start()
    p3.start()
    p4.start()
