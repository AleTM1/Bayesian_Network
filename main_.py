from structure_learn import hill_climbing
from dataset_generator import dataset_gen as generator


def main():
    states_path = '/home/alessandro/Documenti/IA/Datasets/Asia/states.csv'
    prob_table_path = '/home/alessandro/Documenti/IA/Datasets/Asia/prob.csv'
    structure_path = '/home/alessandro/Documenti/IA/Datasets/Asia/structure.csv'
    data = generator.importer.csv_to_numpy(states_path, prob_table_path, structure_path)
    n = 5000
    dataset = generator.dataset_gen(data[0], data[1], data[2], n)
    print("Dataset generato")
    result = hill_climbing.BIC_hill_climbing(data[0], dataset)

    print("FINITO. Dimensione del dataset: ", n)
    print(result[0].get_matrix())
    print("Score: ", result[1])


if __name__ == '__main__':
    main()