class PhysicalAddress:
    def __init__(self, frame_no: int, offset):
        self.frame_no = frame_no
        self.offset = offset

    def __repr__(self):
        return f'(frame_no: {self.frame_no}, offset: {self.offset})'
