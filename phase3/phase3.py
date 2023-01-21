from process import Process
from var import Var


class Memory:
    def __init__(self, size: int, frame_size: int):
        self.frames_count = [0] * (size // frame_size)


def main():
    frame_no = 0
    frame_size = 400

    process_a = Process(name='A', vars=[
        Var('var1', 4),
        Var('var2', 8),
        Var('var3', 240),
        Var('var4', 148),
        Var('var5', 300),
    ], frame_size=frame_size)

    process_b = Process(name='B', vars=[
        Var('var1', 4),
        Var('var2', 8),
        Var('var3', 240),
        Var('var4', 148),
        Var('var5', 300),
    ], frame_size=frame_size)

    processes = [process_a, process_b]

    for process in processes:
        for page_no in range(process.pages_count):
            process.set_frame(page_no, frame_no)
            frame_no += 1

        print(process)

        for var in process.vars:
            la = process.get_var_logical_address(var.name)
            pa = process.translate_logical_address(la)
            print(var, la, pa)

    # print(process_a)
    # print(process_b)
    # la = process_b.get_var_logical_address('var4')
    # pa = process_b.translate_logical_address(la)
    # print(la)
    # print(pa)


if __name__ == '__main__':
    main()
