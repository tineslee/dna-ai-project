import numpy as np
from neural_network import NeuralNetwork

# Cria rede neural simples
nn = NeuralNetwork(input_size=2, hidden_size=3, output_size=1)

# Dados de treino (exemplo: porta lógica OR)
x = np.array([[0,1],[1,0],[1,1],[0,0]])
y = np.array([[1],[1],[1],[0]])

# Treina a rede
for epoch in range(1000):
    nn.train(x, y, lr=0.1)

# Testa resultados
print("Saídas após treino:")
for sample in x:
    print(sample, "->", nn.forward(sample))
