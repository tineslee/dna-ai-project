# Testes Escalados – AND, XOR e Iris

## Objetivo
Validar se o modelo híbrido mantém desempenho superior em problemas mais complexos, além da porta OR.

---

## Configuração dos Experimentos
- **Porta AND**
  - Entradas: [[0,0],[0,1],[1,0],[1,1]]
  - Saídas esperadas: [[0],[0],[0],[1]]
  - Épocas: 1000
  - LR: 0.1
- **Porta XOR**
  - Entradas: [[0,0],[0,1],[1,0],[1,1]]
  - Saídas esperadas: [[0],[1],[1],[0]]
  - Épocas: 2000
  - LR: 0.1
- **Dataset Iris**
  - 150 amostras, 4 features
  - 3 classes (one-hot encoding)
  - Épocas: 2000
  - LR: 0.05

---

## Resultados Obtidos

| Experimento | Modelo Puro (MSE) | Modelo Híbrido (MSE) | Observações |
|-------------|-------------------|----------------------|-------------|
| AND         | 0.1130            | 0.0078               | Híbrido muito superior |
| XOR         | 0.1755            | 0.1877               | Puro ligeiramente melhor; híbrido variou mais |
| Iris        | 0.0289            | 0.0026               | Híbrido extremamente superior |

---

## Conclusão
- **Porta AND:** O modelo híbrido reduziu drasticamente o erro, confirmando maior capacidade de aprendizado.  
- **Porta XOR:** O resultado foi mais equilibrado; o híbrido apresentou maior variabilidade e não superou o modelo puro neste caso.  
- **Dataset Iris:** O híbrido teve desempenho muito superior, com erro quase dez vezes menor que o modelo puro.  

Esses resultados mostram que o modelo híbrido é especialmente vantajoso em problemas lineares (AND) e de classificação real (Iris), mas pode apresentar maior variabilidade em problemas não lineares complexos (XOR). Isso reforça a necessidade de analisar a **diversidade genética** e sua relação com o desempenho.
