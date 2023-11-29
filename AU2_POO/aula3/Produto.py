
class Produto:
    def __init__(self, nome, valor, quantidade = 0, marca = '', modelo = ''): 
        self.nome = nome 
        self.valor = valor
        self.quantidade = quantidade
        self.marca = marca
        self.modelo = modelo

    def vender(self, quantidade):
        if (self.quantidade > quantidade):
            print('Não há estoque suficiente.') 
            print('Quantidade maxima:', self.quantidade)
        else:
            self.quantidade -= quantidade

    def comprar(self, quantidade):
        self.quantidade += quantidade

produto = Produto('Celular', 2000, 100, 'Redmi')
produto.comprar(10)
produto.vender(100)

produto1 = Produto('Geladeira', 5000)

produto2 = Produto('Notebook', 4000, 'Del',)

print(produto.__dict__)
print(produto1.__dict__)
print(produto2.__dict__)
        