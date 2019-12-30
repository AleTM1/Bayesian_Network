from structure_learn import csv_converter, hill_climbing


def main():

    data = csv_converter.csv_to_numpy('/home/alessandro/Documenti/IA/Datasets/Asia/variable_value.csv', '/home/alessandro/Documenti/IA/Datasets/Asia/ASIA10k.csv')
    result = hill_climbing.BIC_hill_climbing(data[0], data[1])

    print("FINITO")
    print(result[0].get_matrix())
    print("Score: ", result[1])


if __name__ == '__main__':
    main()