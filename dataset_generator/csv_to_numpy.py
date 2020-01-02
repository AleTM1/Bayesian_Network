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
        dominio.append(int(states_array[i]))

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
        row = next(prob_reader)
        r_prob = np.zeros(len(row))
        for j in range(len(row)):
            r_prob[j] = row[j]
        probabilities.append(r_prob)

    prob_file.close()

    return dominio, structure_matrix, probabilities

