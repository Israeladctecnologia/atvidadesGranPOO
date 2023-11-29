numeros = [2, 4, 6, 8]

'''
resultado = []
for n in numeros:
    resultado.append(n*2)
print(numeros, resultado)
'''

resultado = map(lambda n : n*5, numeros )
print(numeros, list(resultado))