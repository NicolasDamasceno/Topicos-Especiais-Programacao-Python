1. subir o arquivo para o notebook

2. importar a biblioteca Pandas

3. carregar o arquivo .csv: criar uma variável dataset que receberá a chamada de **pd.read_csv(arquivo)**

Não esquecer do separador ";"

4. mostre o dataset

5. mostre os tipos de dados do dataset: comando: dtypes. Quais os tipos de dados das colunas deste dataset?


6. mostre a estatística descritiva das colunas: quilometragem e valor. Qual o significado dessas informações?

7. Obtenha mais informações do dataset com a função info(). Tem alguma coluna com dados nulos? Se sim, qual a coluna e quantos  dados nulos possui?

8. Com base no Dataset que estamos trabalhando, defina uma função para mostrar a quilometragem média de todos os carros.  Sabendo  que a formula é:

Km_media = km_total / (ano_atual - ano_fabricação)

A função tem que receber como parâmetros: o dataset e o ano atual.
Execute a função e mostre o resultado.

9. Utilizando a pesquisa com queries, faça:
a) mostre os carros com motor "Diesel V8"
b) pesquise por carros com motor 1.0 8v usados com preço inferior a R$ 100.000
c) pesquise por carros com km média de até 10.000 km com Motor 1.8 16v
d) liste os tipos de motores cadastrados 
e) liste os carros com câmbio automático com valor abaixo de R$ 100.000
f) liste os carros novos com "freios ABS" que custam acima de R$ 100.000
g) liste os carros novos ou usados com km média abaixo de 10.000 km que custam até R$ 100.000