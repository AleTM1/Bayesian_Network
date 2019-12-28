import csv_converter
import hill_climbing


def main():

    data = csv_converter.csv_to_numpy('/home/alessandro/Documenti/IA/Datasets/Alarm/variable_value.csv', '/home/alessandro/Documenti/IA/Datasets/Alarm/ALARM10k.csv')
    best_structure = hill_climbing.BIC_hill_climbing(data[0], data[1])

    print(best_structure.get_matrix())


if __name__ == '__main__':
    main()