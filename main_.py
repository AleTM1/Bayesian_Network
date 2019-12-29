import csv_converter
import hill_climbing
import numpy as np


def main():

    data = csv_converter.csv_to_numpy('/home/alessandro/Documenti/IA/Datasets/Asia/variable_value.csv', '/home/alessandro/Documenti/IA/Datasets/Asia/ASIA10k.csv')
    best_structure = hill_climbing.BIC_hill_climbing(data[0], data[1])

    """""
    domini = [2, 3, 2, 4]
    data = np.zeros((5, 4))
    #data[0, 2] = 1  #
    data[1, 0] = 1
    data[1, 1] = 2
    data[1, 2] = 1
    data[1, 3] = 3
    data[2, 0] = 1
    data[2, 1] = 1
    data[2, 3] = 1
    #data[3, 1] = 2   #
    data[4, 0] = 1
    data[4, 1] = 1
    data[4, 2] = 1
    data[4, 3] = 2
    best_structure = hill_climbing.BIC_hill_climbing(domini, data)
    """

    print("FINITO")
    print(best_structure.get_matrix())


if __name__ == '__main__':
    main()