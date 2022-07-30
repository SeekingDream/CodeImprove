

class AbstractCode:
    def __init__(self, code, label):
        self.code = code
        self.label = label

        self.ast = self.extract_ast()
        self.cfg = self.extract_cfg()

    def extract_ast(self):  # TODO
        return self.code

    def extract_cfg(self):  # TODO
        return self.code
