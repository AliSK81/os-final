from multiprocessing import Process, Queue, Value

import LeftSide
import RightSide
from Peterson import Locker


def main():
    street = Value('d', 0)
    id = Value('d', 1)

    car_list1 = Queue(maxsize=10)
    car_list2 = Queue(maxsize=10)

    producer_locker = Locker()
    consume_locker = Locker()

    prod1 = Process(target=RightSide.producer, args=(car_list1, id, producer_locker))
    cons1 = Process(target=RightSide.consumer, args=(car_list1, street, consume_locker))
    prod1.start()
    cons1.start()

    prod2 = Process(target=LeftSide.producer, args=(car_list2, id, producer_locker))
    cons2 = Process(target=LeftSide.consumer, args=(car_list2, street, consume_locker))
    prod2.start()
    cons2.start()


if __name__ == '__main__':
    main()
