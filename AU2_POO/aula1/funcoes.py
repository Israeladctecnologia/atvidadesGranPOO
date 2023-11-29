# Uso de Fuçoes sem o return.
'''
def dividir(n1, n2):
    resultado = n1 / n2
    print(f'{n1} / {n2} = {resultado}')

dividir(80, 5)
dividir(10, 2)
'''

# Funcoes com o return.

def somar(n1,n2):
    return n1 + n2

def subtrair(n1, n2):
    return n1 - n2

def multiplicar(n1, n2):
    return n1 * n2

def dividir(n1, n2):
    if n2 == 0:
        return " Não é possível dividir por 0." 
    else:
        resultado = n1 / n2
        return resultado 

def calcular(n1, n2, operador):
    match operador:
        case '+': return somar(n1, n2)
        case '-': return subtrair(n1, n2)
        case '*': return multiplicar(n1, n2)
        case '/': return subtrair(n1, n2)
        case other: 'Operador não encontrado'

print(calcular(445, 8, '/'))





    

'''
divisao = dividir(80,5)
print('O resultado é ', divisao)

print(' Resultado ', dividir(10,2))

resultado = dividir(30, 2)
soma =  20 + resultado
print('Soma é', soma)

dividir(40, 5)
'''        





