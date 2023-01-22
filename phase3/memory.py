class Memory:
    def __init__(self, size: int, frame_size: int):
        self.frames_count = size // frame_size
        self.frames = [''] * self.frames_count

    def set_frame(self, frame_no: int, process_name: str):
        self.frames[frame_no] = process_name

    def get_remaining_frames(self):
        return self.frames.count('')

    def is_allocated(self, frame_no):
        return self.frames[frame_no] != ''

    def deallocate(self, frame_no):
        self.frames[frame_no] = ''

    def is_process_loaded(self, process_name):
        for frame in self.frames:
            if frame.startswith(process_name):
                return True
        return False

    def __repr__(self):
        return f'Memory:\n' \
               f'remaining_frames: {self.get_remaining_frames()}\n' \
               f'frames: {self.frames}\n'
