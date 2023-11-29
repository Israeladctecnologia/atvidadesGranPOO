from abc import ABC, abstractmethod

class Imovel(ABC):
    def __init__(self, nome, uf, valor, endereco = '', area = ''):
        self._nome = nome
        self._uf = uf
        self._valor = valor
        self._endereco = endereco
        self._area = area

    @property
    def nome(self):
        return self._nome
    def uf(self):
        return self._uf
    def valor(self):
        return self._valor
    def endereco(self):
        return self._endereco
    def area(self):
        return self._area
    
    @nome.setter
    def nome(self, nome):
        self._nome = nome
    @uf.setter
    def uf(self, uf):
        self._uf = uf
    @valor.setter
    def valor(self, valor):
        self._valor = valor
    @endereco.setter
    def endereco(self, endereco):
        self._endereco = endereco
    @area.setter
    def area(self, area):
        self._area = area



    def detalhar(self):
        print(self.__dict__)

    def calcular_impostos(self):
        return self.valor * 0.02
    
    @abstractmethod
    def aluguelSugerido(self):
        ...
    
class ImovelResidencia(Imovel):
    def __init__(self, nome, uf, valor, endereco='', area=''):
        super().__init__(nome, uf, valor, endereco = '', area = '')
        self.quartos = 0
        self.piscina = False

    def aluguelSugerido(self):
        return self.valor * 0.001

class ImoverComercial(Imovel):
    pass

    def aluguelSugerido(self):
        return self.valor * 0.015

class ImovelRural:
    def __init__(self, hectares = '', curral = '', produtiva = True):
        self.hectares = hectares
        self.curral = curral
        self.produtiva = produtiva

    def mesPlantacao(self, mes):
        match int(mes):
            case 1: print('Milho')
            case 2: print('Feijão')
            case 3: print('Soja')
            case other: print('Algodão')

class Fazenda(Imovel, ImovelRural):
    ...

    def aluguelSugerido(self):
        return self.valor * 0.025

fazenda = Fazenda('Modelo', 'PR', 15000000)
fazenda.detalhar()
print(fazenda.calcular_impostos())
fazenda.mesPlantacao(7)            


casa = ImovelResidencia('Vila Martins', 'PR', 500000)
casa.detalhar()
print(casa.aluguelSugerido())