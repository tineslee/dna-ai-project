# hybrid_model.py
import numpy as np
from dna_cycle import evolutionary_cycle
from neural_network import NeuralNetwork

def dna_to_vector(sequence):
    """
    Converte uma sequência de DNA em vetor numérico.
    A, T, C, G → valores arbitrários para entrada da rede neural.
    """
    mapping = {"A": 0, "T": 1, "C": 2, "G": 3}
    return np.array([mapping[base] for base in sequence.nucleotides])

def hybrid_training(data_set, generations=5, threshold=0.5, hidden_size=4, epochs=500, lr=0.1):
    """
    Integra ciclo evolutivo com rede neural.
    - Gera biblioteca genética
    - Converte DNA em vetores
    - Treina rede neural com dados originais + vetores genéticos
    """
    # Ciclo evolutivo
    library = evolutionary_cycle(data_set, generations, threshold)

    # Converte DNA em vetores
    dna_vectors = [dna_to_vector(seq) for seq in library]

    # Dados originais (exemplo: porta OR)
    x = np.array([[0,1],[1,0],[1,1],[0,0]])
    y = np.array([[1],[1],[1],[0]])

    # Combina dados originais + vetores genéticos
    combined_inputs = []
    for i in range(len(x)):
        # concatena entrada original com um vetor genético aleatório
        dna_vec = dna_vectors[i % len(dna_vectors)]
        combined = np.concatenate((x[i], dna_vec))
        combined_inputs.append(combined)

    combined_inputs = np.array(combined_inputs)

    # Cria rede neural híbrida
    nn = NeuralNetwork(input_size=combined_inputs.shape[1], hidden_size=hidden_size, output_size=1)

    # Treina rede neural
    for epoch in range(epochs):
        nn.train(combined_inputs, y, lr=lr)

    return nn, combined_inputs, y
