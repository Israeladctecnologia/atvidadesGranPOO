
numeros = [1, 2, 3, 4, 5, 6, 7, 55, 60, 77, 89]

resultado = filter(lambda n: n % 2 == 0, numeros)
print(list(resultado))