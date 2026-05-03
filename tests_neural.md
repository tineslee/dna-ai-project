# Teste da Rede Neural

## Objetivo
Validar se a rede neural simples (NumPy) consegue aprender a lógica da porta OR.

## Configuração
- Arquivo: `neural_network.py`
- Função: `NeuralNetwork`
- Dados de treino:
  - Entradas: [[0,1], [1,0], [1,1], [0,0]]
  - Saídas esperadas: [[1], [1], [1], [0]]
- Número de épocas: 1000
- Taxa de aprendizado: 0.1

## Resultados
- Saída após treino:
  - [0,1] → ~1.0
  - [1,0] → ~1.0
  - [1,1] → ~1.0
  - [0,0] → ~0.0

## Conclusão
A rede neural aprendeu corretamente a lógica da porta OR.
