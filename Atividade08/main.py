'''
Usando os datasets carros.csv, drinks.csv (vinhos), titanic.csv, vgsales.csv (videogames) e anac.csv (voos), escolha pelo menos 2 gráficos adequados para representar os resultados de seus insights para cada dataset acima e plote-os
'''

import matplotlib.pyplot as plt
import pandas as pd
import mplcursors


# Carros
df_carros = pd.read_csv('datasets/carros.csv', delimiter=';')

# Gráfico 1: Barras - Quilometragem dos carros
df_carros_agrupados = df_carros.groupby('Ano')['Quilometragem'].mean().reset_index()

plt.figure(figsize=(10, 6))
plt.plot(df_carros_agrupados['Ano'], df_carros_agrupados['Quilometragem'], marker='o', color='blue')
plt.xlabel('Ano')
plt.ylabel('Quilometragem Média')
plt.title('Quilometragem Média dos Carros por Ano de Fabricação')
plt.xticks(df_carros_agrupados['Ano'], rotation=45)
plt.tight_layout()
plt.show()

# Gráfico 2: Pizza - Percentual de carros zero km ou não
zero_km_counts = df_carros['Zero_km'].value_counts()
labels = ['Não', 'Sim']
colors = ['red', 'green']

plt.figure(figsize=(8, 8))
plt.pie(zero_km_counts, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
plt.title('Percentual de Carros Zero Km')
plt.axis('equal')
plt.show()


# Vinhos
df_drinks = pd.read_csv('datasets/drinks.csv')

# Gráfico 1: Barras - Top 10 países com maior consumo de cerveja
top_10_beer = df_drinks.nlargest(10, 'beer_servings')

plt.figure(figsize=(12, 8))
plt.bar(top_10_beer['country'], top_10_beer['beer_servings'], color='orange')
plt.xlabel('País')
plt.ylabel('Consumo de Cerveja (servings)')
plt.title('Top 10 Países com Maior Consumo de Cerveja')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Gráfico 2: Dispersão - Consumo total de álcool vs Consumo de vinho
plt.figure(figsize=(10, 6))
scatter = plt.scatter(df_drinks['total_litres_of_pure_alcohol'], df_drinks['wine_servings'], color='purple')
plt.xlabel('Consumo Total de Álcool (litros)')
plt.ylabel('Consumo de Vinho (servings)')
plt.title('Consumo Total de Álcool vs Consumo de Vinho')
plt.grid(True)

cursor = mplcursors.cursor(scatter, hover=True)
cursor.connect('add', lambda sel: sel.annotation.set_text(df_drinks['country'][sel.index]))

plt.tight_layout()
plt.show()


# Titanic
df_titanic = pd.read_csv('datasets/titanic.csv')

# Gráfico 1: Barras - Distribuição de sobreviventes por classe
survived_by_class = df_titanic.groupby('Pclass')['Survived'].sum().reset_index()

plt.figure(figsize=(10, 6))
plt.bar(survived_by_class['Pclass'], survived_by_class['Survived'], color='blue')
plt.ylabel('Número de Sobreviventes')
plt.title('Distribuição de Sobreviventes por Classe')
plt.xticks([1, 2, 3], ['1ª Classe', '2ª Classe', '3ª Classe'])
plt.tight_layout()
plt.show()


# Gráfico 2: Setores - Proporção de sobreviventes e não sobreviventes
survived_counts = df_titanic['Survived'].value_counts()
labels = ['Não Sobreviveu', 'Sobreviveu']
colors = ['red', 'green']

plt.figure(figsize=(8, 8))
plt.pie(survived_counts, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
plt.title('Proporção de Sobreviventes e Não Sobreviventes')
plt.axis('equal')
plt.tight_layout()
plt.show()


# Videogames

df_vgsales = pd.read_csv('datasets/vgsales.csv')

# Gráfico 1: Colunas - Vendas globais dos 10 jogos mais vendidos
top_10_games = df_vgsales.nlargest(10, 'Global_Sales')

plt.figure(figsize=(12, 8))
plt.bar(top_10_games['Name'], top_10_games['Global_Sales'], color='blue')
plt.xlabel('Jogo')
plt.ylabel('Vendas Globais (milhões)')
plt.title('Top 10 Jogos Mais Vendidos')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Gráfico 2: Setores - Distribuição das vendas globais por plataforma
platform_sales = df_vgsales.groupby('Platform')['Global_Sales'].sum().reset_index()
platform_sales = platform_sales.nlargest(5, 'Global_Sales')  

plt.figure(figsize=(8, 8))
plt.pie(platform_sales['Global_Sales'], labels=platform_sales['Platform'], autopct='%1.1f%%', startangle=140)
plt.title('Distribuição das Vendas Globais por Plataforma')
plt.axis('equal')
plt.tight_layout()
plt.show()

# Voos
df_anac = pd.read_csv('datasets/anac.csv', delimiter=';', encoding='latin1')

# Gráfico 1: Barras - Top 10 destinos com maior número de assentos comercializados
assentos_por_destino = df_anac.groupby('ICAO Aeródromo Destino')['Assentos Comercializados'].sum().reset_index()
top_10_destinos = assentos_por_destino.nlargest(10, 'Assentos Comercializados')

plt.figure(figsize=(12, 8))
plt.bar(top_10_destinos['ICAO Aeródromo Destino'], top_10_destinos['Assentos Comercializados'], color='blue')
plt.xlabel('Destino')
plt.ylabel('Assentos Comercializados')
plt.title('Top 10 Destinos com Maior Número de Assentos Comercializados')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# Gráfico 2: Pizza - Distribuição percentual dos assentos comercializados por empresa aérea
assentos_por_empresa = df_anac.groupby('ICAO Empresa Aérea')['Assentos Comercializados'].sum().reset_index()

plt.figure(figsize=(8, 8))
plt.pie(assentos_por_empresa['Assentos Comercializados'], labels=assentos_por_empresa['ICAO Empresa Aérea'], autopct='%1.1f%%', startangle=140)
plt.title('Distribuição Percentual dos Assentos Comercializados por Empresa Aérea')
plt.axis('equal')
plt.tight_layout()
plt.show()
