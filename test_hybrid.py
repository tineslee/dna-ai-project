# test_hybrid.py
from hybrid_model import hybrid_training

# Conjunto de dados binários
data_set = ["1010", "1100", "0000", "1111"]

# Treina modelo híbrido
nn, inputs, outputs = hybrid_training(data_set, generations=3, threshold=0.5, epochs=1000)

print("\nResultados do modelo híbrido:")
for i, sample in enumerate(inputs):
    print(sample, "->", nn.forward(sample), "esperado:", outputs[i])
