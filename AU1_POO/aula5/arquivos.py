arquivo = open('nomes.txt', 'w')

arquivo.write('Joao\n')
arquivo.write('Orion\n')
arquivo.write('Israel\n')

arquivo.close()

with open('nomes.txt' , 'r+') as arquivoLeitura:
    for linha in arquivoLeitura:
        print(linha)
