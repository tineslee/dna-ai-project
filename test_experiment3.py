# test_experiment3.py
import numpy as np
from neural_network import NeuralNetwork
from hybrid_model import hybrid_training

def mse(y_true, y_pred):
    return np.mean((y_true - y_pred) ** 2)

# --- Rede Neural Pura ---
x = np.array([[0,1],[1,0],[1,1],[0,0]])
y = np.array([[1],[1],[1],[0]])

nn_pure = NeuralNetwork(input_size=2, hidden_size=3, output_size=1)
for epoch in range(1000):
    nn_pure.train(x, y, lr=0.1)

pred_pure = np.array([nn_pure.forward(sample) for sample in x])
mse_pure = mse(y.flatten(), pred_pure.flatten())

# --- Rede Neural Híbrida ---
data_set = ["1010", "1100", "0000", "1111"]
nn_hybrid, inputs, outputs = hybrid_training(data_set, generations=3, threshold=0.5, epochs=1000)

pred_hybrid = np.array([nn_hybrid.forward(sample) for sample in inputs])
mse_hybrid = mse(outputs.flatten(), pred_hybrid.flatten())

# --- Comparação ---
print("=== Comparação Direta ===")
print("MSE Rede Neural Pura:", mse_pure)
print("MSE Rede Neural Híbrida:", mse_hybrid)
