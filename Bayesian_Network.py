import numpy as np
import math

class BayesianNetwork:
    def __init__(self, N):
        self.matrix = np.zeros((N, N))

    def score_function(self):
