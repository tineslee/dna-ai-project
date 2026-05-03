**Descrição**
Este projeto explora a integração de processos evolutivos inspirados em DNA artificial com redes neurais artificiais, avaliando como a diversidade genética influencia a robustez e a capacidade de generalização dos modelos de aprendizado.

O sistema foi desenvolvido do zero em Python, com módulos independentes que simulam codificação em DNA, mutação, recombinação, seleção natural e ciclo evolutivo, além da implementação de uma rede neural híbrida.

**Estrutura do Projeto**

    dna_encoding.py → codificação de dados binários em DNA artificial.

    dna_mutation.py → mutação e recombinação de sequências.

    dna_selection.py → cálculo de fitness e seleção natural.

    dna_cycle.py → integração dos processos evolutivos em ciclos de gerações.

    neural_network.py → implementação da rede neural (forward e backpropagation).

    hybrid_model.py → integração entre DNA evoluído e rede neural.

    plot_entropy.py → geração de gráficos de entropia genética por geração.

    tests/ → scripts de teste (AND, XOR, Iris).

    docs/ → documentação e figuras (gráficos de entropia, resultados).

 **Instalação**
Clone o repositório e instale as dependências:
``
git clone https://github.com/seu-usuario/dna-ai-project.git
cd dna-ai-project
pip install -r requirements.txt
``
**Como Executar**
Testes básicos
Porta AND:
``
python tests/test_and.py
``
Porta XOR:
``
python tests/test_xor.py
``
Dataset Iris:
``
python tests/test_iris.py
``
Análise de diversidade genética
``
python plot_entropy.py
``
**Resultados Obtidos**

    Porta AND: híbrido muito superior (MSE ≈ 0.0078 vs 0.1130).

    Porta XOR: puro ligeiramente melhor (MSE ≈ 0.1755 vs 0.1877).

    Dataset Iris: híbrido extremamente superior (MSE ≈ 0.0026 vs 0.0289).

    Diversidade genética: entropia inicial ≈ 1.75, convergindo rapidamente para ≈ 0.93.

**Bibliotecas Utilizadas**

    NumPy → operações matriciais.

    scikit-learn → datasets e pré-processamento.

    matplotlib → visualização gráfica.

**Disponibilidade**

Este repositório é público e pode ser utilizado para fins acadêmicos e de pesquisa.
Para citar em artigos, utilize:

    Thais, DNA AI Project: Integração de Evolução Genética com Redes Neurais, GitHub, 2026. Disponível em: https://github.com/seu-usuario/dna-ai-project (github.com in Bing)
