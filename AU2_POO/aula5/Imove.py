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
    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def uf(self):
        return self._uf
    @uf.setter
    def uf(self, uf):
        self._uf = uf
    
    @property
    def valor(self):
        return self._valor
    @valor.setter
    def valor(self, valor):
        self._valor = valor

    @property
    def endereco(self):
        return self._endereco
    @endereco.setter
    def endereco(self, endereco):
        self._endereco = endereco

    @property
    def area(self):
        return self._area
    @area.setter
    def area(self, area):
        self._area = area
    
    def detalhar(self):
        print(self.__dict__)

    def calcular_impostos(self):
        return self._valor * 0.02
    
    @abstractmethod
    def aluguelSugerido(self):
        ...
    
class ImovelResidencia(Imovel):
    def __init__(self, nome, uf, valor, endereco='', area=''):
        super().__init__(nome, uf, valor, endereco = '', area = '')
        self._quartos = 0
        self._piscina = False

    def aluguelSugerido(self):
        return self._valor * 0.001

class ImoverComercial(Imovel):
    pass

    def aluguelSugerido(self):
       return self_valor * 0.015
    
    def calcular_impostos(self):
         match self._uf:
            case 'RJ' : taxa = 0.04
            case 'DF' : taxa = 0.05
            case 'PR' : taxa = 0.02
            case other : taxa = 0.01
             
         return self._valor * taxa  

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


print('#############################')
casa = ImovelResidencia('Vila Martins', 'PR', 500000)
casa.detalhar()
print(casa.aluguelSugerido())

print('############################')
fazenda = Fazenda('Modelo', 'PR', 15000000)
fazenda.detalhar()
print(fazenda.calcular_impostos())
fazenda.mesPlantacao(7)    

print('#############################')

clinica = ImoverComercial('clinica', 'RJ', 400000,)
clinica.detalhar()
print(clinica.calcular_impostos())

