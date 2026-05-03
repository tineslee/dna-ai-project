# test_and.py
import numpy as np
from neural_network import NeuralNetwork
from hybrid_model import hybrid_training

def mse(y_true, y_pred):
    return np.mean((y_true - y_pred) ** 2)

# Dados da porta AND
x = np.array([[0,0],[0,1],[1,0],[1,1]])
y = np.array([[0],[0],[0],[1]])

# Rede neural pura
nn_pure = NeuralNetwork(input_size=2, hidden_size=3, output_size=1)
for epoch in range(1000):
    nn_pure.train(x, y, lr=0.1)
pred_pure = np.array([nn_pure.forward(sample) for sample in x])
print("MSE Pura AND:", mse(y.flatten(), pred_pure.flatten()))

# Rede neural híbrida
data_set = ["1010", "1100", "0000", "1111"]
nn_hybrid, inputs, outputs = hybrid_training(data_set, generations=3, threshold=0.5, epochs=1000)
pred_hybrid = np.array([nn_hybrid.forward(sample) for sample in inputs])
print("MSE Híbrida AND:", mse(outputs.flatten(), pred_hybrid.flatten()))
