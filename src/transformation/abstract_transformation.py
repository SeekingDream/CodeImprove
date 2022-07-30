from ..abstract_code import AbstractCode


class AbstractTransformation:
    def __init__(self):
        self.name = None

    def transform(self, x: AbstractCode) -> AbstractCode:
        pass
