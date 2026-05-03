# test_classification.py
import numpy as np
from sklearn.datasets import load_iris
from sklearn.preprocessing import OneHotEncoder
from neural_network import NeuralNetwork
from hybrid_model import hybrid_training

def mse(y_true, y_pred):
    return np.mean((y_true - y_pred) ** 2)

# Carregar Iris dataset
iris = load_iris()
x = iris.data
y = iris.target.reshape(-1,1)

# One-hot encoding das classes
encoder = OneHotEncoder(sparse_output=False)
y_encoded = encoder.fit_transform(y)

# Rede neural pura
nn_pure = NeuralNetwork(input_size=x.shape[1], hidden_size=6, output_size=3)
for epoch in range(2000):
    nn_pure.train(x, y_encoded, lr=0.05)
pred_pure = np.array([nn_pure.forward(sample) for sample in x])
print("MSE Pura Iris:", mse(y_encoded.flatten(), pred_pure.flatten()))

# Rede neural híbrida
data_set = ["1010", "1100", "0000", "1111"]
nn_hybrid, inputs, outputs = hybrid_training(data_set, generations=5, threshold=0.5, epochs=2000, hidden_size=6)
pred_hybrid = np.array([nn_hybrid.forward(sample) for sample in inputs])
print("MSE Híbrida Iris:", mse(outputs.flatten(), pred_hybrid.flatten()))
