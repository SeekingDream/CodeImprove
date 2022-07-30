from typing import List

from .abstract_policy import AbstractPolicy


from ..abstract_model import AbstractModel
from ..abstract_model import AbstractCode


class ModelCarloNode:
    def __init__(self, x: AbstractCode, s, parent=None):
        self.x = x
        self.parent = parent
        self.children = []
        self.score = s


class ModelCarloTreeSearch(AbstractPolicy):
    def __init__(self, model: AbstractModel, corpus: List[AbstractCode], config):
        super(ModelCarloTreeSearch, self).__init__(model, corpus, config)

    def select_node(self):             # TODO
        return self.root

    def run(self, x: AbstractCode):
        s = self.model.get_uncertainty(x)
        self.root = ModelCarloNode(x, s, None)
        self.best_candidate, self.best_score = x, s

        status = 0
        while status == 0:
            current_node = self.select_node()
            new_x_list = [T.transform(current_node) for T in self.TRANSFORM_LIST]
            for new_x in new_x_list:
                new_s = self.model.get_uncertainty(new_x)
                new_node = ModelCarloNode(new_x, new_s, current_node)
                current_node.children.append(new_node)
                self.iteration += 1
            status = self.is_stop()
