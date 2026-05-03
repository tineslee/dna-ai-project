# dna_encoding.py
class DNASequence:
    def __init__(self, nucleotides: str):
        self.nucleotides = list(nucleotides)

    def __repr__(self):
        return "".join(self.nucleotides)

def encode_to_dna(data: str) -> DNASequence:
    """
    Converte uma string binária em uma sequência de DNA artificial.
    Exemplo: "1010" -> "CG"
    """
    mapping = {"00": "A", "01": "T", "10": "C", "11": "G"}
    dna = ""
    for i in range(0, len(data), 2):
        bits = data[i:i+2]
        dna += mapping.get(bits, "A")  # fallback para 'A'
    return DNASequence(dna)
