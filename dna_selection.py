# dna_selection.py
from dna_encoding import DNASequence

def fitness(sequence: DNASequence) -> float:
    """
    Calcula a aptidão de uma sequência de DNA.
    Critério: proporção de bases 'C' e 'G' (mais estáveis).
    """
    score = sum(1 for base in sequence.nucleotides if base in ["C", "G"])
    return score / len(sequence.nucleotides)

def natural_selection(library: list, threshold: float) -> list:
    """
    Aplica seleção natural: mantém apenas sequências com fitness >= threshold.
    """
    return [seq for seq in library if fitness(seq) >= threshold]
