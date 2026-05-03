# Teste de Fitness e Seleção Natural

## Objetivo
Validar se as funções de fitness e seleção natural avaliam corretamente a aptidão das sequências de DNA e filtram as menos adaptadas.

## Configuração
- Arquivo: `dna_selection.py`
- Funções: `fitness`, `natural_selection`
- Sequências iniciais:
  - seq1 = "1010" → CC
  - seq2 = "1100" → GA
  - seq3 = "0000" → AA
- Threshold: 0.5

## Resultados obtidos
- Fitness calculado:
  - CC → 1.0
  - GA → 0.5
  - AA → 0.0
- Seleção natural (threshold=0.5):
  - Mantidas: CC, GA
  - Eliminada: AA

## Conclusão
As funções de fitness e seleção natural funcionam corretamente, mantendo apenas sequências com aptidão suficiente e descartando as menos adaptadas.
