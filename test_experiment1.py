# test_experiment1.py
import numpy as np
from neural_network import NeuralNetwork

def mse(y_true, y_pred):
    return np.mean((y_true - y_pred) ** 2)

# Dados da porta OR
x = np.array([[0,1],[1,0],[1,1],[0,0]])
y = np.array([[1],[1],[1],[0]])

# Rede neural pura
nn = NeuralNetwork(input_size=2, hidden_size=3, output_size=1)
for epoch in range(1000):
    nn.train(x, y, lr=0.1)

pred = np.array([nn.forward(sample) for sample in x])
print("Saídas:", pred.flatten())
print("MSE:", mse(y.flatten(), pred.flatten()))
