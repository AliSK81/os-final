class Var:
    def __init__(self, name: str, size: int):
        self.name = name
        self.size = size

    def __repr__(self):
        return f'(name: {self.name}, size: {self.size})'
