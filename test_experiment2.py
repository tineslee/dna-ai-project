# test_experiment2.py
import numpy as np
from hybrid_model import hybrid_training

def mse(y_true, y_pred):
    return np.mean((y_true - y_pred) ** 2)

# Dados binários iniciais
data_set = ["1010", "1100", "0000", "1111"]

# Treina modelo híbrido
nn, inputs, outputs = hybrid_training(data_set, generations=3, threshold=0.5, epochs=1000)

pred = np.array([nn.forward(sample) for sample in inputs])
print("Saídas:", pred.flatten())
print("MSE:", mse(outputs.flatten(), pred.flatten()))
