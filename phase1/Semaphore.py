from multiprocessing import Value, Array, Queue


class Locker:

    def __init__(self, n: int):
        self.val = Value('i', 1)
        self.arr = Array('i', [0] * n)
        self.queue = Queue(n)

    def lock(self, i: int):
        self.val.value -= 1
        if self.val.value < 0:
            self.arr[i] = 0
            self.queue.put(i)
            while True:
                if self.arr[i] == 1:
                    break

    def unlock(self, i: int):
        self.val.value += 1
        if self.val.value <= 0:
            j = self.queue.get()
            self.arr[j] = 1
        self.arr[i] = 0
