from memory import Memory
from process import Process
from var import Var


def main():
    frame_size = 400
    mem_size = 1200
    pages_count = mem_size // frame_size

    process_a = Process(name='A', vars=[
        Var('var1', 4),
        Var('var2', 8),
        Var('var3', 240),
        Var('var4', 148),
        Var('var5', 300),
    ], page_size=frame_size, pages_count=pages_count)

    process_b = Process(name='B', vars=[
        Var('var1', 4),
        Var('var2', 8),
        Var('var3', 240),
        Var('var4', 148),
        Var('var5', 300),
    ], page_size=frame_size, pages_count=pages_count)

    processes = [process_a, process_b]

    frame_no = 0

    mem = Memory(mem_size, frame_size)
    print(mem)

    for process in processes:
        frames_required = process.allocated_bytes // frame_size + 1

        if frames_required <= mem.get_remaining_frames():

            for page_no in range(frames_required):
                mem.set_frame(frame_no, f'{process.name}{page_no}')

                process.set_frame(page_no, frame_no)
                frame_no += 1

        elif frames_required <= mem.frames_count:
            print('to replace')

        else:
            print('no space')

    print(mem)

    for process in processes:
        print(process)

    process_a.print_var_addresses('var5')


if __name__ == '__main__':
    main()
