import pandas as pd
import numpy as np

# Passo 1: Ler o conjunto de dados para um DataFrame
df = pd.read_csv("./Atividade04/heart.csv")

# Passo 2: Verificar as primeiras linhas do DataFrame
print("Primeiras linhas do DataFrame:")
print(df.head())

# Passo 3: Verificar as últimas linhas do DataFrame
print("\nÚltimas linhas do DataFrame:")
print(df.tail())

# Passo 4: Verificar as dimensões do DataFrame
print("\nDimensões do DataFrame:")
print(df.shape)

# Passo 5: Verificar as informações sobre as colunas do DataFrame
print("\nInformações sobre o DataFrame:")
df.info()

# Passo 6: Verificar as estatísticas descritivas básicas do DataFrame
print("\nEstatísticas descritivas do DataFrame:")
print(df.describe())

# Passo 7: Verificar dados ausentes
print("\nDados ausentes no DataFrame:")
print(df.isnull().sum())

# Passo 8: Selecionar uma coluna específica como array Numpy
colunaEspecifica = df['age'].to_numpy()  # Exemplo com a coluna 'age'
print("\nColuna 'age' como Numpy array:")
print(colunaEspecifica)

# Passo 9: Selecionar duas ou mais colunas específicas como DataFrame
colunasESpecificas = df[['age', 'sex']]  # Exemplo com as colunas 'age' e 'sex'
print("\nColunas 'age' e 'sex' como DataFrame:")
print(colunasESpecificas)

# Passo 10: Selecionar linhas específicas usando loc[]
linhaEspecifica = df.loc[0]  # Exemplo: Selecionar a primeira linha
print("\nPrimeira linha do DataFrame:")
print(linhaEspecifica)

# Passo 11: Selecionar linhas específicas com base em uma ou mais condições
linhasFiltradas = df.loc[(df['age'] > 50) & (df['chol'] > 200)]  # Exemplo
print("\nLinhas onde 'age' > 50 e 'chol' > 200:")
print(linhasFiltradas)