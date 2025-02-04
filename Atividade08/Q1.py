import pandas as pd
import matplotlib.pyplot as plt

# Carregando o primeiro dataset sobre os dados de voos da ANAC
arquivo = './Atividade08/anac.CSV'
dataset1 = pd.read_csv(arquivo, encoding='latin1',sep=';')

# Dataset completo
print(f'ANAC: \n{dataset1}')

# Realizando um gráfico horizontal das empresas e a quantidade de assentos comercializados de cada uma
assentos_por_destinos = dataset1.groupby('ICAO Aeródromo Destino')['Assentos Comercializados'].sum().reset_index()
top3 = assentos_por_destinos.nlargest(3,'Assentos Comercializados')
empresas = ['AZU', 'GLO', 'TAM']
 
# Criando o gráfico
plt.bar(empresas,top3['Assentos Comercializados'],color='g')
plt.xlabel('Empresas Aeréas', size=20)
plt.ylabel('Assentos Comerzializados', size=20)
plt.title('Assentos Comercializados em 2020')
plt.show()

# Gráfico de Pizza sobre a porporção de cada empresa sobre assentos comercializados
assentos_empresa = dataset1.groupby('ICAO Empresa Aérea')['Assentos Comercializados'].sum().reset_index()

plt.pie(assentos_empresa['Assentos Comercializados'], labels=assentos_empresa['ICAO Empresa Aérea'])
plt.title('Assentos comercializados por empresa Aérea')
plt.show()

# Carregando o segundo dataset sobre os dados dos carros
arquivo = './Atividade08/carros.csv'
dataset2 = pd.read_csv(arquivo,sep=';')

# Gráfico de colunas para a quilometragem dos carros com o seu ano de fabricação
carros_km = dataset2.groupby('Ano')['Quilometragem'].mean().reset_index()
plt.bar(carros_km['Ano'], carros_km['Quilometragem'], color='g')
plt.xlabel('Ano')
plt.ylabel('Quilometragem Média')
plt.title('Quilometragem com base no ano dos Veículos')
plt.show()

# Gráfico de pizza para carros zero km ou não
km_zero = dataset2['Zero_km'].value_counts()
plt.pie(km_zero,labels=['Zero_KM', 'KM'], colors=['blue','green'])
plt.title('Percentual de carros 0KM')
plt.show()

# Carregando o terceiro dataset sobre as bebidas
arquivo = './Atividade08/drinks.csv'
dataset3 = pd.read_csv(arquivo,sep=',')

# Criando uma gráfico em barras para os 10 paises com maior consumo de bebidas
top10 = dataset3.nlargest(10,'beer_servings')

plt.bar(top10['country'], top10['beer_servings'], color='blue')
plt.xlabel('Paises')
plt.ylabel('Consumo de Alchool')
plt.title('Rank 10 paises com maior consumo de Alchool')
plt.show()

# Criando um gráfico de barras para comparar o consumo de 3 tipos de bebidas
beer = dataset3['beer_servings'].sum()
wine = dataset3['wine_servings'].sum()
spirit = dataset3['spirit_servings'].sum()
drink_data = [beer, wine, spirit]
label = ['Cerveja', 'Vinho', 'Espumantes']
plt.bar(label, drink_data, color='red')
plt.xlabel('Tipo de Bebida')
plt.ylabel('Consumo Total')
plt.title('Consumo de 3 tipos de Alchool Mundial')
plt.show()

# Carregando o quarto dataset sobre as vítimas do Titanic
arquivo = './Atividade08/titanic_csv.csv'
dataset4 = pd.read_csv(arquivo,sep=',')

# Criando um gráfico de pizza com a proporção de sobreviventes e não sobreviventes
sobreviventes = dataset4['Survived'].value_counts()

plt.pie(sobreviventes, labels=['Falecido', 'Sobrevivente'])
plt.title('Proporção de sobreviventes e falecidos do Titanic')
plt.show()

# Gráfico de pizza da proporção de sobreviventes distrubuídos pelas classes
sobreviventes_classes = dataset4.groupby('Pclass')['Survived'].sum().reset_index()
plt.pie(sobreviventes_classes['Survived'],labels=['1 Classe','2 Classe', '3 Classe'])
plt.title('Distribuição de sobreviventes entre as Classes')
plt.show()

# Carregando o quinto dataset sobre vendas de videos games
arquivo = './Atividade08/vgsales.csv'
dataset5 = pd.read_csv(arquivo,sep=',')

# Criando um gráfico de barras dos 10 jogos mais vendidos
games_top_10 = dataset5.nlargest(10,'Global_Sales')

plt.bar(games_top_10['Name'], games_top_10['Global_Sales'], color='orange')
plt.xlabel('Jogos')
plt.ylabel('Vendas Globais (milhões)')
plt.title('Rank dos 10 jogos mais vendidos no Globo')
plt.show()

# Criando um gráfico de pizza com a distribuição de vendas por publicadora
vendas_publicadora = dataset5.groupby('Publisher')['Global_Sales'].sum().reset_index()
vendas_publicadora = vendas_publicadora.nlargest(5,'Global_Sales')

plt.pie(vendas_publicadora['Global_Sales'], labels=vendas_publicadora['Publisher'])
plt.title('Proporção de vendas globais por Publicadora')
plt.show()