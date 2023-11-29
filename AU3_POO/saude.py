import numpy as np
import pandas as pd


class Pacientes:
    def __init__(self, nome, idade, sexo, peso, altura):
        self.nome = nome 
        self.idade = idade
        self.sexo = sexo
        self.peso = peso
        self.altura = altura

pacientes = {
    "Paciente 1" : Pacientes("Maria", 25,'F', 78, 1.72),
    "Paciente 2" : Pacientes("Orion", 30,'M', 90, 1.80),
    "Paciente 3" : Pacientes("Jose", 70, 'M', 80, 1.75),
    "Paciente 4" : Pacientes("Ana", 25, 'F', 90, 1.70),
}


l_pacientes = [p.__dict__ for p in pacientes.values()]
df_pacientes = pd.DataFrame.from_records(l_pacientes, index= pacientes.keys())
df_pacientes ['IMC'] = df_pacientes.apply(lambda i : i.peso / i.altura **2, axis = 1)

media = np.mean(df_pacientes['IMC'])
sobrepeso = df_pacientes[df_pacientes['IMC'] > 25]
percentual = len(sobrepeso) / len(df_pacientes) *100

print(df_pacientes)


