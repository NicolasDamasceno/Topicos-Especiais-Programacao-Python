Exercício - NumPy com Dados de Desmatamento
Utilize o dataset disponível no link Deforestation Dataset - Kaggle, que contém dados sobre a
cobertura florestal mundial e taxas de desmatamento de diferentes países entre os anos de
2020 e 2022. As colunas principais do dataset representam:
• Country Name: Nome do país.
• Year: Ano de registro (2020 a 2022).
• Forest Area (% of land area): Área de cobertura florestal como porcentagem da área
total do país.
• Deforestation Rate (% annual change): Taxa anual de desmatamento em
porcentagem.

Instruções
1. Carregamento do Dataset:
• Importe o arquivo utilizando o método numpy.loadtxt, ajustando para ignorar o
cabeçalho e processar adequadamente os dados categóricos (nome do país) e
numéricos.
• Converta os dados numéricos em um array NumPy para facilitar a análise.
2. Manipulação dos Dados:
• Use as funcionalidades do NumPy para processar e analisar os dados relacionados ao
desmatamento e cobertura florestal.
3. Produza pelo menos 5 relatórios (insights):
1. Identifique os 10 países com maior taxa de desmatamento em cada ano (2020, 2021,
2022).
2. Liste os 5 países que apresentaram o menor índice de cobertura florestal em 2022.
3. Determine a média de variação anual na taxa de desmatamento para cada continente
(se o dataset incluir essa informação).
4. Calcule a média global de cobertura florestal para os anos de 2020 a 2022.
5. Identifique o país com a maior queda percentual na área florestal durante o período
analisado.

Observações
• Certifique-se de tratar dados ausentes ou inconsistentes no arquivo CSV.