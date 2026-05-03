# neural_network.py
import numpy as np

class NeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size):
        self.w1 = np.random.randn(input_size, hidden_size)
        self.w2 = np.random.randn(hidden_size, output_size)

    def activate(self, x):
        return 1 / (1 + np.exp(-x))  # função sigmoide

    def forward(self, x):
        self.hidden = self.activate(np.dot(x, self.w1))
        output = self.activate(np.dot(self.hidden, self.w2))
        return output

    def train(self, x, y, lr=0.01):
        # Forward pass
        output = self.forward(x)
        # Backprop simplificado
        error = y - output
        d_output = error * output * (1 - output)
        d_hidden = np.dot(d_output, self.w2.T) * self.hidden * (1 - self.hidden)

        # Atualiza pesos
        self.w2 += np.dot(self.hidden.T, d_output) * lr
        self.w1 += np.dot(x.T, d_hidden) * lr
