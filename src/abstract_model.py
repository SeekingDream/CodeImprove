import torch.nn as nn

from .abstract_code import AbstractCode
from .uncertainty import UNCERTAINTY_LIST


class AbstractModel:
    UNCERTAINTY_LIST = UNCERTAINTY_LIST

    def __init__(self, model, config):
        self.model = model
        self.config = config

        u_id = self.config['uncertainty_type']
        self.u = self.UNCERTAINTY_LIST[u_id](model)

    def predict(self, x: AbstractCode):      # TODO
        return self.model.predict(x)

    def get_uncertainty(self, x: AbstractCode):
        return self.u.get_uncertainty(x)
