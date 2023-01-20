from multiprocessing import Process, Queue, Value

import LeftSide
import RightSide


def main():
    street = Value('d', 0)
    id = Value('d', 1)

    car_list1 = Queue(maxsize=10)
    car_list2 = Queue(maxsize=10)

    prod1 = Process(target=RightSide.producer, args=(car_list1, id))
    cons1 = Process(target=RightSide.consumer, args=(car_list1, street))
    prod1.start()
    cons1.start()

    prod2 = Process(target=LeftSide.producer, args=(car_list2, id))
    cons2 = Process(target=LeftSide.consumer, args=(car_list2, street))
    prod2.start()
    cons2.start()


if __name__ == '__main__':
    main()
