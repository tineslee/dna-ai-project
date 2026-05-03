# test_selection.py
from dna_encoding import encode_to_dna
from dna_selection import fitness, natural_selection

# Criando biblioteca de sequências
seq1 = encode_to_dna("1010")  # CC
seq2 = encode_to_dna("1100")  # GA
seq3 = encode_to_dna("0000")  # AA

library = [seq1, seq2, seq3]

print("Sequências iniciais:")
for seq in library:
    print(seq, "-> fitness:", fitness(seq))

# Aplicando seleção natural
selected = natural_selection(library, threshold=0.5)

print("\nSequências após seleção natural (threshold=0.5):")
for seq in selected:
    print(seq, "-> fitness:", fitness(seq))
