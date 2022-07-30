
class AbstractUncertainty:
    def __init__(self, model):
        self.u_name = None
        self.model = model

    def get_uncertainty(self, x):
        pass