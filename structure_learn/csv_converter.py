import csv
import numpy as np

""""
Partendo dal file csv del dataset e da un file csv che specifica le modalità che possono essere assunte da ogni stato,
la funzione restituisce un numpy array 2D con i valori numerici per ogni tupla del dataset.
La funzione restituisce anche un array di dimensione N con la dimensione del dominio delle N variabili
"""


def csv_to_numpy(table_path, dataset_path):

    dataset_array = []

    table = open(table_path, 'r')
    table_reader = csv.reader(table, delimiter=',')
    table_title = next(table_reader)
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
            table_index = table_title.index(states[i]) + 1
            while table_title[table_index] != row[i]:
                table_index += 1
                k += 1
            data_row.append(k)
        dataset_array.append(data_row)
        line += 1

    dataset = np.array(dataset_array)
    # creazione array delle modalità
    dominio = []
    i = 0
    for j in range(1, num_states + 1, 1):
        i += 1
        if j < num_states:
            k = 0
            while table_title[i] != states[j]:
                i += 1
                k += 1
            dominio.append(k)
        else:
            dominio.append(len(table_title) - i)

    raw_data.close()

    return dominio, dataset


def main():
    data = csv_to_numpy('/home/alessandro/Documenti/IA/Datasets/Alarm/variable_value.csv', '/home/alessandro/Documenti/IA/Datasets/Alarm/ALARM10k.csv')
    print(data[0])
    print(data[1])


if __name__ == '__main__':
    main()




