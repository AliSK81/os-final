class LogicalAddress:
    def __init__(self, page_no: int, offset):
        self.page_no = page_no
        self.offset = offset

    def __repr__(self):
        return f'(page_no: {self.page_no}, offset: {self.offset})'
