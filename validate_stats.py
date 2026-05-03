# validate_stats.py
import numpy as np
from neural_network import NeuralNetwork
from hybrid_model import hybrid_training

def mse(y_true, y_pred):
    return np.mean((y_true - y_pred) ** 2)

def run_pure():
    x = np.array([[0,1],[1,0],[1,1],[0,0]])
    y = np.array([[1],[1],[1],[0]])
    nn = NeuralNetwork(input_size=2, hidden_size=3, output_size=1)
    for epoch in range(500):
        nn.train(x, y, lr=0.1)
    pred = np.array([nn.forward(sample) for sample in x])
    return mse(y.flatten(), pred.flatten())

def run_hybrid():
    data_set = ["1010", "1100", "0000", "1111"]
    nn, inputs, outputs = hybrid_training(data_set, generations=3, threshold=0.5, epochs=500)
    pred = np.array([nn.forward(sample) for sample in inputs])
    return mse(outputs.flatten(), pred.flatten())

# Rodar várias vezes
runs = 30
results_pure = [run_pure() for _ in range(runs)]
results_hybrid = [run_hybrid() for _ in range(runs)]

print("Rede Pura - média:", np.mean(results_pure), "desvio:", np.std(results_pure))
print("Rede Híbrida - média:", np.mean(results_hybrid), "desvio:", np.std(results_hybrid))
