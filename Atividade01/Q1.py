import csv

class Pais:
    def __init__(self):
        self.nome = None

    def detalharPais(self,arquivo,pais):
        with open(arquivo, 'r') as file:
            leitor_csv = csv.reader(file)
            next(leitor_csv)
            for linha in leitor_csv:
                if linha[0] == pais:
                    self.nome = linha[0]
                    print(f'País: {linha[0]}\nPorções de Cerveja: {linha[1]}mL\nPorções de Espumantes: {linha[2]}mL\nPorções de Vinho: {linha[3]}mL\nMédia de Consumo por Habitante: {linha[4]}L')

class drinks:
    def __init__(self) -> None:
        self.paises = []

    def lerArquivo(self,arquivo):
        with open(arquivo, 'r') as file:
            leitor_csv = csv.reader(file)
            next(leitor_csv)
            for linha in leitor_csv:
                self.paises.append(linha)
                print(f'\nPaís: {linha[0]}\nPorções de Cerveja: {linha[1]}mL\nPorções de Espumantes: {linha[2]}mL\nPorções de Vinho: {linha[3]}mL\nMédia de Consumo por Habitante: {linha[4]}L\n')

    def maiorMediaHabitante(self,arquivo):
        with open(arquivo, 'r') as file:
            leitor_csv = csv.reader(file)
            next(leitor_csv)
            maiorPais = 0
            nome = None
            for linha in leitor_csv:
                if float(linha[4]) > maiorPais:
                    maiorPais = float(linha[4])
                    nome = linha[0]
            return print(f'Pais com maior média: {nome}\nMédia de Consumo por Habitante: {maiorPais}L')


drink = drinks()
drink.lerArquivo('drinks.csv')
drink.maiorMediaHabitante('drinks.csv')

pais = Pais()
pais.detalharPais('drinks.csv', 'Brazil')
