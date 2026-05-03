# Teste de Codificação Binário → DNA

## Objetivo
Validar se a função `encode_to_dna` converte corretamente strings binárias em sequências de DNA artificiais.

## Configuração
- Arquivo: `dna_encoding.py`
- Função: `encode_to_dna`
- Mapeamento utilizado:
  - 00 → A
  - 01 → T
  - 10 → C
  - 11 → G

## Entradas usadas
- "1010"
- "1100"

## Saídas obtidas
- "1010" → CC
- "1100" → GA

## Conclusão
A função de codificação está funcionando corretamente de acordo com o mapeamento definido.  
A saída inicial esperada (CG, GA) era apenas ilustrativa; o resultado real (CC, GA) confirma que o algoritmo aplica o mapeamento binário → DNA de forma consistente.
