from structure_learn import hill_climbing
from dataset_generator import dataset_gen as generator, csv_to_numpy


def main():
    n = 10000
    t = 8
    states_path = 'resources/states.csv'
    prob_table_path = 'resources/prob.csv'
    structure_path = 'resources/structure.csv'
    data = csv_to_numpy.csv_to_numpy(states_path, prob_table_path, structure_path)
    dataset = generator.dataset_gen(data[0], data[1], data[2], n)
    print("Dataset generato")
    result = hill_climbing.BIC_hill_climbing(data[0], dataset, t)

    print("FINITO. Dimensione del dataset: ", n)
    print(result[0].get_matrix())
    print("Score: ", result[1])


if __name__ == '__main__':
    main()