# dna_mutation.py
import random
from dna_encoding import DNASequence

def mutate(sequence: DNASequence) -> DNASequence:
    """
    Aplica mutação em uma posição aleatória da sequência de DNA.
    """
    nucleotides = ["A", "T", "C", "G"]
    pos = random.randint(0, len(sequence.nucleotides) - 1)
    sequence.nucleotides[pos] = random.choice(nucleotides)
    return sequence

def recombine(seq1: DNASequence, seq2: DNASequence) -> DNASequence:
    """
    Recombina duas sequências de DNA em um ponto de corte aleatório.
    """
    cut_point = random.randint(0, min(len(seq1.nucleotides), len(seq2.nucleotides)) - 1)
    new_seq = seq1.nucleotides[:cut_point] + seq2.nucleotides[cut_point:]
    return DNASequence("".join(new_seq))
