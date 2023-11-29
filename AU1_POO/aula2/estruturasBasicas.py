aluno = input("--> Nome do aluno: ")
turma = input("--> Turma: ")

n1 = float(input("Digite nota 1: -->")) 
n2 = float(input("Digite nota 2: -->"))
n3 = float(input("Digite nota 3: -->"))
n4 = float(input("Digite nota 4: -->"))

soma = n1 + n2 + n3 + n4
media = soma / 4

print("Media do", aluno, turma , media)

if media >= 7:
    print('APROVADO')
elif media < 5:
    print('REPROVADO')
else:
    print("RECUPERAÇÃO")