import pandas as pd

# Caminho do arquivo CSV
arquivo = './Atividade05/202001.CSV'

# Ler o conjunto de dados para um DataFrame
df = pd.read_csv(arquivo, encoding='latin1', sep=';')
print(f'DataFrame completo:\n{df}')

# 1. Verificar as primeiras linhas
print("1. Primeiras linhas do DataFrame:")
print(df.head())

# 2. Verificar as últimas linhas
print("\n2. Últimas linhas do DataFrame:")
print(df.tail())

# 3. Verificar as dimensões do DataFrame
print("\n3. Dimensões do DataFrame:")
print(f"Linhas: {df.shape[0]}, Colunas: {df.shape[1]}")

# 4. Verificar as informações sobre as colunas
print("\n4. Informações sobre o DataFrame:")
print(df.info())

# 5. Verificar as estatísticas descritivas básicas
print("\n5. Estatísticas descritivas:")
print(df.describe())

# 6. Selecionar colunas específicas
colunas_especificas = df[['ICAO Empresa Aérea', 'ICAO Aeródromo Origem']]
print("\n6. Selecionar colunas (usando colchetes):")
print(colunas_especificas.head())

# 7. Selecionar linhas específicas
linhas_especificas = df.loc[0:4, :]  # Selecionando as 5 primeiras linhas
print("\n7. Selecionar linhas específicas (usando loc):")
print(linhas_especificas)

# 8. Filtrar linhas com base em uma condição
linhas_filtradas = df[(df['ICAO Empresa Aérea'] == 'AZU') & (df['Assentos Comercializados'] > 10)]
print("\n8. Filtrar linhas com base em uma condição:")
print(linhas_filtradas.head())

# 9. Agrupar dados com groupby()
grupo = df.groupby('ICAO Empresa Aérea')['Assentos Comercializados'].mean()
print("\n9. Agrupar dados (média de assentos por empresa aérea):")
print(grupo)

# 10. Ordenar o DataFrame com base em uma ou mais colunas
df_ordenado = df.sort_values(by='Assentos Comercializados', ascending=False)
print("\n10. Ordenar o DataFrame por Assentos Comercializados (decrescente):")
print(df_ordenado.head())

# Insight: Analisar destinos mais frequentes para voos filtrados
filtro = df[(df['ICAO Empresa Aérea'] == 'AZU') & (df['Assentos Comercializados'] > 10)]
print('\nDestino mais frequente para os voos filtrados: ')
destino_mais_frequente = filtro['ICAO Aeródromo Destino'].value_counts().head(1)
print(destino_mais_frequente)