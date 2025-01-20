import pandas as pd

# 1. Carregar o arquivo .csv
arquivo = './Atividade07/carros.csv'
dataset = pd.read_csv(arquivo, sep=';')

# 2. Corrigir o nome da coluna 'Valor,,,,,,,,,' e converter para numérico
dataset.rename(columns={'Valor,,,,,,,,,': 'Valor'}, inplace=True)
dataset['Valor'] = dataset['Valor'].str.replace(',', '').astype(float)

# 3. Mostrar o dataset
print("Dataset:")
print(dataset.head())

# 4. Mostrar os tipos de dados do dataset
print("\nTipos de dados:")
print(dataset.dtypes)

# 5. Estatística descritiva de Quilometragem e Valor
print("\nEstatísticas descritivas:")
print(dataset[['Quilometragem', 'Valor']].describe())

# 6. Verificar informações gerais e dados nulos
print("\nInformações gerais do dataset:")
print(dataset.info())

# 7. Função para calcular quilometragem média
def calcular_km_media(dataset, ano_atual):
    dataset['Km_media'] = dataset['Quilometragem'] / (ano_atual - dataset['Ano'])
    return dataset[['Nome', 'Km_media']]

# Usando a função
ano_atual = 2025
km_media = calcular_km_media(dataset, ano_atual)
print("\nQuilometragem média dos carros:")
print(km_media)

# 8. Consultas com queries:
# a) Carros com motor "Diesel V8"
print("\nCarros com motor 'Diesel V8':")
print(dataset.query("Motor == 'Motor Diesel V8'"))

# b) Carros com motor 1.0 8v usados com preço inferior a R$ 100.000
print("\nCarros com motor 1.0 8v usados com preço < R$ 100.000:")
print(dataset.query("Motor == 'Motor 1.0 8v' and Zero_km == False and Valor < 100000"))

# c) Carros com km média <= 10.000 e Motor 1.8 16v
print("\nCarros com km média <= 10.000 e Motor 1.8 16v:")
print(dataset.query("Km_media <= 10000 and Motor == 'Motor 1.8 16v'"))

# d) Tipos de motores cadastrados
print("\nTipos de motores cadastrados:")
print(dataset['Motor'].unique())

# e) Carros com câmbio automático abaixo de R$ 100.000
print("\nCarros com câmbio automático e valor < R$ 100.000:")
print(dataset.query("Valor < 100000 and Acessórios.str.contains('Câmbio automático')", engine='python'))

# f) Carros novos com freios ABS que custam acima de R$ 100.000
print("\nCarros novos com 'freios ABS' e valor > R$ 100.000:")
print(dataset.query("Zero_km == True and Valor > 100000 and Acessórios.str.contains('Freios ABS')", engine='python'))

# g) Carros novos ou usados com km média < 10.000 e valor <= R$ 100.000
print("\nCarros com km média < 10.000 e valor <= R$ 100.000:")
print(dataset.query("Km_media < 10000 and Valor <= 100000"))