import numpy as np


class BayesianNetwork:
    def __init__(self, N):
        self.matrix = np.zeros((N, N))
