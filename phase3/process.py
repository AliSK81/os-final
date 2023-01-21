from logical_address import LogicalAddress
from physical_address import PhysicalAddress
from var import Var


class Process:
    def __init__(self, name: str, vars: [Var], frame_size: int):
        self.name = name
        self.vars = vars

        self.pages_count: int
        self.page_table: []

        self.vars_info = dict()
        self.__init_vars_info(frame_size)

    def __init_vars_info(self, frame_size: int):
        summ = 0
        page_no = 0

        for var in self.vars:
            page_no = summ // frame_size
            offset = summ % frame_size
            self.vars_info[var.name] = LogicalAddress(page_no=page_no, offset=offset)
            summ += var.size

        self.pages_count = page_no + 1
        self.page_table = [0] * self.pages_count

    def set_frame(self, page_no: int, frame_no: int):
        self.page_table[page_no] = frame_no

    def get_frame(self, page_no):
        return self.page_table[page_no]

    def get_var_logical_address(self, var_name: str):
        return self.vars_info[var_name]

    def translate_logical_address(self, logical_address: LogicalAddress):
        frame_no = self.page_table[logical_address.page_no]
        offset = logical_address.offset
        return PhysicalAddress(frame_no=frame_no, offset=offset)

    def __repr__(self):
        return f'''Process: {self.name}
        vars: {self.vars}
        vars_info: {self.vars_info}
        pages_count: {self.pages_count}
        page_table: {self.page_table}
        '''
