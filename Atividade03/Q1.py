import numpy as np

# Criando o dataset utilizando o loadtxt do Numpy
dataForest = np.loadtxt("./Atividade03/goal15.forest_shares.csv", delimiter=",", skiprows=1, dtype=str)

# Removendo aspas da coluna iso3c
dataForest[:,0] = np.char.strip(dataForest[:, 0], '"')

# Convertando os dados em um Array Numpy
dataForest = np.array(dataForest, dtype=object)
for i in range(1, dataForest.shape[1]):
    dataForest[:, i] = np.where(dataForest[:, i] == '', np.nan, dataForest[:, i]).astype(float)

# Printando o Dataset com Array
print(f'Dataset de desmatamento: \n{dataForest}')

# Obtendo os países com maior taxa de desmatamento em 2000
countryDesfro2000 = np.argsort(dataForest[:, 1])[::-1][:10]

# Obtendo os países com maior taxa de desmatamento em 2020
countryDesfro2020 = np.argsort(dataForest[:, 2])[::-1][:10]

# Obtendo os seus nomes
country2000 = dataForest[countryDesfro2000, 0]
country2020 = dataForest[countryDesfro2020, 0]

print(f'\n10 países com maior taxa de desmatamento em 2000: \n{country2000}')
print(f'\n10 países com maior taxa de desmatamento em 2020: \n{country2020}')

# Obtendo os 5 países com menor indice florestal em 2020
florestLow2020 = np.argsort(dataForest[:,3])[:5]

# Obtendo os nomes dos países
country2020 = dataForest[florestLow2020, 0]

print(f'\nOs 5 países com menor indice florestal em 2020: \n{country2020}')

# Calculando a média global de cobertura florestal de 2000 a 2020
globalMediaArea = np.nanmean(dataForest[:, 3])

print(f'\nMédia global de cobertura florestal de 2000 a 2020: {globalMediaArea}')

# Calculando o percentual de queda das floresta durante 2000 e 2020
percentageFlorest = dataForest[:, 3] - dataForest[:,1]

# Obtetendo o pais com maior indice de queda percentual da área florestal
florestMaxLoss = np.nanargmax(percentageFlorest)

# Obtendo o nome do pais
florestMaxLossCountry = dataForest[florestMaxLoss, 0]

print(f"\nPaís com a maior queda percentual na área florestal durante o período analisado: {florestMaxLossCountry}")