from multiprocessing import Value, Array


class Locker:

    def __init__(self):
        self.flag = Array('i', [0] * 2)
        self.turn = Value('i', 1)

    def lock(self, i: int):
        self.flag[i] = 1
        self.turn.value = 1 - i
        while self.flag[1 - i] and self.turn.value == 1 - i:
            continue

    def unlock(self, i: int):
        self.flag[i] = 0
