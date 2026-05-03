# Validação Estatística – Rede Neural Pura vs. Híbrida

## Objetivo
Avaliar consistência dos resultados comparando média e desvio padrão do MSE em múltiplas execuções.

## Configuração
- Script: `validate_stats.py`
- Rodadas: 30 execuções independentes
- Modelos: Rede Neural Pura vs. Rede Neural Híbrida

## Resultados obtidos
- Rede Pura:
  - Média MSE: 0.0980
  - Desvio padrão: 0.0356
- Rede Híbrida:
  - Média MSE: 0.0600
  - Desvio padrão: 0.0483

## Conclusão
O modelo híbrido apresentou menor média de erro, confirmando maior capacidade de aprendizado.  
Entretanto, o desvio padrão mais alto sugere que a diversidade genética aumenta a variabilidade dos resultados.  
Isso indica que o híbrido é mais poderoso, mas também mais sensível às condições iniciais do ciclo evolutivo.
