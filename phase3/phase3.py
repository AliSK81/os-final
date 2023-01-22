from memory import Memory
from process import Process
from var import Var

frame_size = 400
mem_size = 4000

pages_count = mem_size // frame_size

curr_frame_no = 0

mem = Memory(mem_size, frame_size)

queue = list()


def load_process(process: Process):
    global frame_size
    global mem_size
    global pages_count
    global curr_frame_no
    global mem
    global queue

    frames_required = process.get_required_frames()

    if frames_required <= mem.get_remaining_frames():

        for page_no in range(frames_required):
            mem.set_frame(curr_frame_no, f'{process.name}{page_no}')

            process.set_frame(page_no, curr_frame_no)
            curr_frame_no += 1

        queue.append(process)

    else:

        while frames_required > 0:
            dropped_process = queue.pop(0)

            for frame_no in range(mem.frames_count):
                if mem.frames[frame_no].startswith(dropped_process.name):
                    print(f'deallocated {mem.frames[frame_no]}')
                    mem.deallocate(frame_no)

            frames_required -= dropped_process.get_required_frames()

        for page_no in range(process.get_required_frames()):

            for frame_no in range(mem.frames_count):

                if not mem.is_allocated(frame_no):
                    print(f'frame {frame_no} is not allocated, so replaced with {process.name}{page_no}.')

                    mem.set_frame(frame_no, f'{process.name}{page_no}')

                    process.set_frame(page_no, frame_no)
                    frames_required -= 1
                    page_no += 1
                    break


disk = dict()


def main():
    global mem
    global disk

    disk['A'] = Process(name='A', vars=[
        Var('var1', 4),
        Var('var2', 8),
        Var('var3', 240),
        Var('var4', 148),
        Var('var5', 300),
    ], page_size=frame_size, pages_count=pages_count)

    disk['B'] = Process(name='B', vars=[
        Var('var1', 4),
        Var('var2', 8),
        Var('var3', 240),
        Var('var4', 148),
        Var('var5', 300),
    ], page_size=frame_size, pages_count=pages_count)

    print(mem)

    request('A', 'var2')

    print(mem)

    request('B', 'var5')

    print(mem)


def request(process_name: str, var_name: str):
    global disk
    global mem

    if not mem.is_process_loaded(process_name):
        load_process(disk[process_name])

    disk[process_name].print_var_addresses(var_name)


if __name__ == '__main__':
    main()
