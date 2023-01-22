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

    curr_frame_no = 0

    mem = Memory(mem_size, frame_size)

    queue = list()

    for process in processes:

        print(mem)

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

                print(mem)

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

    print(mem)

    process_a.print_var_addresses('var5')


if __name__ == '__main__':
    main()
