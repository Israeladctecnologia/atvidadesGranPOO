numero = [10, 20, 30, 40, 50, 60] # Lista, array para substituir variaveis individuais.

carros = ['Pálio', 'Gol', 'Virtus', 'Ka', 'Onix']
print('1 -->', carros)

carros.append('Kombi')
print('2-->', carros)

carros.remove('Gol')
print('3 -->', carros)

del carros[3]
print('4 -->', carros)

'''carros = sorted(carros)
print('5 -->', carros)'''

for carro in carros:
    print(carro)


