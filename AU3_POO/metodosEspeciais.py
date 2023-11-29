import data

class Categoria:
    def __init__(self, tipo):
        self.tipo = tipo

    def taxaAgua(self, consumo):

        print(data.formatarData())

        match self.tipo:
            case 'Restaurante': return consumo * 1
            case 'Clinica': return consumo * 2
            case 'Hotel': return consumo * 2.5

class Imovel:

    imposto = 0

    def __init__(self, nome, quartos, suites):
        self.nome = nome
        self.quartos = quartos
        self.suites = suites

    def __add__(self, other):
        somaSelf = self.quartos + self.suites
        somaOther = other.quartos + other.suites
        return somaSelf + somaOther

    def __gt__(self, other):
        somaSelf = self.quartos + self.suites
        somaOther = other.quartos + other.suites
        return somaSelf > somaOther
    
    def __str__(self):
        return str(self.__dict__)

    def detalhar(self):
        return self.__dict__

    def somarAposentos(self):
        return self.quartos + self.suites
    
    @staticmethod
    def metodoEstatistico():
        print('Chamou sem objeto')

    @classmethod
    def metodoClasse(cls):
        print('Chamou', cls.imposto)
    
    
   

casarao = Imovel('Casarão', 3, 4)
mansao = Imovel('Mansão', 6, 7)

categoria = Categoria('Hotel')
hotel = Imovel('Hotel do Chico', 0, 150)
hotel.categoria = categoria
print(hotel.categoria.taxaAgua(500))

#print(casarao)
#print(casarao.somarAposentos())

#soma = casarao + mansao
#print(soma)
#print(casarao > mansao)
#print(mansao)
