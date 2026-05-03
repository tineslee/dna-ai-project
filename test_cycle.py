# test_cycle.py
from dna_cycle import evolutionary_cycle

# Conjunto de dados binários
data_set = ["1010", "1100", "0000", "1111"]

# Executa ciclo evolutivo
final_library = evolutionary_cycle(data_set, generations=5, threshold=0.5)

print("\nSequências finais na biblioteca:")
for seq in final_library:
    print(seq)
