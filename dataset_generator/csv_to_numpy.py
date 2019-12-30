import csv
import numpy as np


def csv_to_numpy(states_path, prob_table_path, structure_path):

    #   array con nome degli stati e domini
    states_file = open(states_path, 'r')
    table_reader = csv.reader(states_file, delimiter=',')
    states_array = next(table_reader)
    states_file.close()
    num_states = int(len(states_array)/2)

    #   creazione array domini
    dominio = []
    for i in range(1, len(states_array), 2):
        dominio.append(states_array[i])

    #   matrice di incidenza
    structure_file = open(structure_path, 'r')
    structure_reader = csv.reader(structure_file, delimiter=',')
    structure_matrix = np.zeros((num_states, num_states))
    for i in range(num_states):
        row = next(structure_reader)
        for j in range(num_states):
            structure_matrix[i, j] = row[j]
    structure_file.close()

    #  array con probabilità
    probabilities = []
    prob_file = open(prob_table_path, 'rt')
    prob_reader = csv.reader(prob_file, delimiter=',')
    next(prob_reader)
    for i in range(num_states):
        probabilities.append(next(prob_reader))

    prob_file.close()

    return dominio, structure_matrix, probabilities


def main():
    states_path = '/home/alessandro/Documenti/IA/Datasets/Asia/states.csv'
    prob_table_path = '/home/alessandro/Documenti/IA/Datasets/Asia/prob.csv'
    structure_path = '/home/alessandro/Documenti/IA/Datasets/Asia/structure.csv'
    data = csv_to_numpy(states_path, prob_table_path, structure_path)
    print(data[0])
    print(data[1])
    print(data[2])


if __name__ == '__main__':
    main()
