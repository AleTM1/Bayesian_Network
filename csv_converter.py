import csv
import numpy as np

""""
Partendo dal file csv del dataset e da un file csv che specifica le modalità che possono essere assunte da ogni stato,
la funzione restituisce un numpy array 2D con i valori numerici per ogni tupla del dataset
"""


def csv_to_numpy(table_path, dataset_path):

    dataset_array = []

    table = open(table_path, 'r')
    table_reader = csv.reader(table, delimiter=',')
    table_array = next(table_reader)
    table.close()

    raw_data = open(dataset_path, 'rt')
    data_reader = csv.reader(raw_data, delimiter=',')
    states = next(data_reader)
    num_states = len(states)

    line = 0
    for row in data_reader:
        data_row = []
        for i in range(0, num_states, 1):
            k = 0
            table_index = table_array.index(states[i]) + 1
            while table_array[table_index] != row[i]:
                table_index += 1
                k += 1
            data_row.append(k)
        dataset_array.append(data_row)
        line += 1

    dataset = np.array(dataset_array)
    print(dataset)
    raw_data.close()

    return dataset


def main():
    csv_to_numpy('/home/alessandro/Documenti/IA/Datasets/Alarm/variable_value.csv', '/home/alessandro/Documenti/IA/Datasets/Alarm/ALARM10k.csv')


if __name__ == '__main__':
    main()




