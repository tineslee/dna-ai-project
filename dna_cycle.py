import random
from dna_encoding import encode_to_dna
from dna_mutation import mutate, recombine
from dna_selection import fitness, natural_selection

def evolutionary_cycle(data_set, generations: int, threshold: float):
    """
    Executa o ciclo evolutivo completo:
    - Codificação dos dados em DNA
    - Mutação
    - Recombinação
    - Seleção natural
    """
    # Biblioteca inicial
    library = [encode_to_dna(data) for data in data_set]

    for gen in range(generations):
        print(f"\nGeração {gen+1}:")
        
        # Mutação
        for seq in library:
            if random.random() < 0.3:  # probabilidade de mutação
                mutate(seq)

        # Recombinação
        for i in range(0, len(library)-1, 2):
            new_seq = recombine(library[i], library[i+1])
            library.append(new_seq)

        # Seleção natural
        library = natural_selection(library, threshold)

        # Mostrar fitness médio da geração
        if len(library) > 0:
            avg_fitness = sum(fitness(seq) for seq in library) / len(library)
            print(f"Fitness médio: {avg_fitness:.2f}")
        else:
            print("Biblioteca vazia após seleção.")

    return library

