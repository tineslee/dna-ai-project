# test_mutation.py
from dna_encoding import encode_to_dna
from dna_mutation import mutate, recombine

# Codificação inicial
seq1 = encode_to_dna("1010")  # CC
seq2 = encode_to_dna("1100")  # GA

print("Sequência original 1:", seq1)
print("Sequência original 2:", seq2)

# Teste de mutação
mutated_seq = mutate(seq1)
print("Sequência após mutação:", mutated_seq)

# Teste de recombinação
recombined_seq = recombine(seq1, seq2)
print("Sequência após recombinação:", recombined_seq)
