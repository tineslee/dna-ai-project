# plot_entropy.py
import matplotlib.pyplot as plt
from dna_cycle import evolutionary_cycle
from collections import Counter
import math

def diversity(library):
    bases = Counter(base for seq in library for base in seq.nucleotides)
    total = sum(bases.values())
    entropy = -sum((count/total) * math.log2(count/total) for count in bases.values())
    return entropy

# Dados iniciais
data_set = ["1010", "1100", "0000", "1111"]

generations = 5
threshold = 0.5
entropies = []

# Rodar ciclo evolutivo e medir entropia a cada geração
library = data_set
for gen in range(1, generations+1):
    library = evolutionary_cycle([str(seq) for seq in library], 1, threshold)
    ent = diversity(library)
    entropies.append(ent)
    print(f"Geração {gen}: Entropia = {ent:.3f}")

# Plotar gráfico
plt.figure(figsize=(8,6))
plt.plot(range(1, generations+1), entropies, marker='o', color='purple')
plt.title("Evolução da Entropia Genética por Geração")
plt.xlabel("Geração")
plt.ylabel("Entropia genética")
plt.grid(True)
plt.show()
