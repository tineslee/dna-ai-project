# analyze_diversity.py
from dna_cycle import evolutionary_cycle
from collections import Counter
import math

def diversity(library):
    # número de sequências únicas
    unique = len(set(str(seq) for seq in library))
    # distribuição de bases
    bases = Counter(base for seq in library for base in seq.nucleotides)
    total = sum(bases.values())
    # entropia genética
    entropy = -sum((count/total) * math.log2(count/total) for count in bases.values())
    return unique, bases, entropy

# Dados iniciais
data_set = ["1010", "1100", "0000", "1111"]

# Ciclo evolutivo com análise de diversidade
generations = 5
threshold = 0.5
library = evolutionary_cycle(data_set, generations, threshold)

# Analisar diversidade final
unique, bases, entropy = diversity(library)

print("\n=== Análise de Diversidade Genética ===")
print("Sequências únicas:", unique)
print("Distribuição de bases:", bases)
print("Entropia genética:", entropy)
