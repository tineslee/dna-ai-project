# Teste de Mutação e Recombinação

## Objetivo
Validar se as funções de mutação e recombinação aplicam corretamente alterações em sequências de DNA artificiais.

## Configuração
- Arquivo: `dna_mutation.py`
- Funções: `mutate`, `recombine`
- Sequências iniciais:
  - seq1 = "1010" → CC
  - seq2 = "1100" → GA

## Resultados obtidos
- Mutação: seq1 → pode alterar uma base aleatória (ex.: CC → CG)
- Recombinação: seq1 + seq2 → nova sequência híbrida (ex.: CG + GA → CGA)

## Conclusão
As funções de mutação e recombinação estão funcionando corretamente, introduzindo diversidade genética nas sequências.
