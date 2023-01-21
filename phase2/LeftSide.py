from multiprocessing import Queue, Value
from time import sleep

from Car import Car
from Peterson import Locker


def producer(queue: Queue, id: Value, locker: Locker):
    print('Producer: Running', flush=True)
    while True:
        if queue.full():
            continue
        locker.lock(0)
        value = Car(id.value)
        id.value += 1
        locker.unlock(0)
        sleep(1)
        queue.put(value)


def consumer(queue: Queue, street: Value, locker: Locker):
    print('Consumer: Running', flush=True)
    while True:
        if queue.empty():
            continue
        locker.lock(0)
        item = queue.get()
        street.value = item.id
        print('LC', 'car id: ', item.id, 'sleep: ', item.time)
        temp = street.value
        sleep(item.time)
        if temp != street.value:
            print('Process conflict!')
        street.value = 0
        locker.unlock(0)
