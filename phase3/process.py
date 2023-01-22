from logical_address import LogicalAddress
from physical_address import PhysicalAddress
from var import Var


class Process:
    def __init__(self, name: str, vars: [Var], page_size: int, pages_count: int):
        self.name = name
        self.vars = vars

        self.page_size = page_size
        self.page_table = [-1] * pages_count
        self.allocated_bytes: int

        self.relative = dict()
        self.__init_vars_relative_address()

    def __init_vars_relative_address(self):
        relative_address = 0

        for var in self.vars:
            self.relative[var.name] = relative_address
            relative_address += var.size
            self.allocated_bytes = relative_address

    def set_frame(self, page_no: int, frame_no: int):
        self.page_table[page_no] = frame_no

    def get_frame(self, page_no):
        return self.page_table[page_no]

    def get_var_relative_address(self, var_name):
        return self.relative[var_name]

    def get_var_logical_address(self, relative_address: int):
        page_no = relative_address // self.page_size
        offset = relative_address % self.page_size
        return LogicalAddress(page_no=page_no, offset=offset)

    def get_var_physical_address(self, logical_address: LogicalAddress):
        frame_no = self.page_table[logical_address.page_no]
        offset = logical_address.offset
        return PhysicalAddress(frame_no=frame_no, offset=offset)

    def get_required_frames(self):
        return self.allocated_bytes // self.page_size + 1

    def __repr__(self):
        return f'''Process: {self.name}
        vars: {self.vars}
        relative: {self.relative}
        page_table: {self.page_table}
        '''

    def print_var_addresses(self, var_name: str):
        ra = self.get_var_relative_address(var_name)
        la = self.get_var_logical_address(ra)
        pa = self.get_var_physical_address(la)
        print(var_name, '\n', 'relative address: ', ra , la, pa)
