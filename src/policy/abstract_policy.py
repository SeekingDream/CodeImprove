from typing import List
from abc import ABC, abstractmethod

from ..abstract_model import AbstractModel
from ..abstract_model import AbstractCode
from ..transformation import TRANSFORM_LIST


class AbstractPolicy:
    TRANSFORM_LIST = TRANSFORM_LIST

    NO_STOP = 0
    REACH_MAX_ITERATION = 1
    REACH_HIGH_SCORE = 2

    def __init__(self, model: AbstractModel, corpus: List[AbstractCode], config):
        self.model = model
        self.corpus = corpus
        self.config = config

        self.root = None
        self.trace_his = None
        self.best_candidate = None
        self.best_score = None
        self.iteration = 0

    def reset(self):
        self.root = None
        self.trace_his = None
        self.best_candidate = None
        self.best_score = None
        self.iteration = 0

    @abstractmethod
    def run(self, x: AbstractCode):
        pass

    def update_status(self, current_x, current_score):
        if current_score > self.best_score:
            self.best_score = current_score
            self.best_candidate = current_x

    def is_stop(self):
        if self.iteration > self.config['max_iter']:
            return self.REACH_MAX_ITERATION
        else:
            if self.best_score > self.config['threshold']:
                return self.REACH_HIGH_SCORE
            else:
                return self.NO_STOP
