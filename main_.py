import score_function as score_f
import Bayesian_Network as BN
import csv_converter
import numpy as np


def main():

    data = csv_converter.csv_to_numpy('/home/alessandro/Documenti/IA/Datasets/Alarm/variable_value.csv', '/home/alessandro/Documenti/IA/Datasets/Alarm/ALARM10k.csv')
    bn = BN.BayesianNetwork(np.size(data[0], 0))

    new_score = score_f.score_function(bn, data[0], data[1])
    print(new_score)


if __name__ == '__main__':
    main()