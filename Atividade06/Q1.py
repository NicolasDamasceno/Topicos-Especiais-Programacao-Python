import pandas as pd

# 1. Importando o DATAFRAME
df = pd.read_csv('./Atividade06/vgsales.csv')
print(df)

# 2. Exibindo as primeiras 5 linhas do DataFrame
primeiras_linhas = df.head(n = 5)
print(primeiras_linhas)

# 3. Estatísticas descritivas para colunas de vendas
print("3. Estatísticas descritivas para as colunas de vendas:")
colunas_vendas = ['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales']
print(df[colunas_vendas].describe())

# 4. Total de vendas globais por gênero
print("\n4. Total de vendas globais por gênero:")
vendas_genero = df.groupby('Genre')['Global_Sales'].sum()
print(vendas_genero)

# 5. Total de vendas globais por plataforma
print("\n5. Total de vendas globais por plataforma:")
vendas_plataforma = df.groupby('Platform')['Global_Sales'].sum()
print(vendas_plataforma)

# 6. Jogo mais vendido
print("\n6. Jogo mais vendido:")
jogo_mais_vendido = df.loc[df['Global_Sales'].idxmax()]
print(jogo_mais_vendido)

# 7. Total de vendas globais por ano
print("\n7. Total de vendas globais por ano:")
vendas_anual = df.groupby('Year')['Global_Sales'].sum()
print(vendas_anual)

# Produzindo insights

# Insight 1: O genêro com maior vendas globais
genero_max = vendas_genero.idxmax()
print(f"\nInsight 1: O gênero com mais vendas globais é '{genero_max}' com um total de {vendas_genero[genero_max]:.2f} milhões de unidades vendidas.")

# Insight 2 - A plataforma que teve maior vendas globais
plataforma_max = vendas_plataforma.idxmax()
print(f"Insight 2: A plataforma com mais vendas globais é '{plataforma_max}' com um total de {vendas_plataforma[plataforma_max]:.2f} milhões de unidades vendidas.")