import numpy as np

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

soma = 0

for n in numeros:
    soma += n

media = soma / len(numeros)
print('Média na mão:', media)

# -----------------------

array_numeros = np.array(numeros)

media = np.mean(array_numeros)
print('Media com np:', media)

# --------------------------

