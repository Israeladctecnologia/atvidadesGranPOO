
try:
    n1 = int(input('Número 1: '))
    n2 = int(input('Número 2: '))

    resultado = n1 / n2
    print(f' Resultado é {resultado}')

except Exception as erro:
    print(f'Ocorreu um erro, {erro}.')

except ZeroDivisionError:
    print('Não é possível dividir por zero.')

except ValueError:
    print('Favor digite somente numeros.')

else:
    print('Rodou perfeitamente.')

finally:
    print('FIM')