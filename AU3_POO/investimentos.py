import pandas as pd
import matplotlib.pyplot as plt 

class Investimentos:
    def __init__(self, nome, valor, taxa, periodo):
        self.nome = nome
        self.valor = valor
        self.taxa = taxa
        self.periodo = periodo

investimentos = {
    'Investimento 1' : Investimentos('Tesouro Direto', 10000, 0.02, 5),
    'Investimento 2' : Investimentos('Açoes', 5000, 0.05, 3),
    'Investimento 3' : Investimentos('Poupanca', 8000, 0.01, 8),
    'Investimento 4' : Investimentos('CDB', 7000, 0.04, 4),
}

l_investimentos = [i.__dict__ for i in investimentos.values()]
df_investimentos = pd.DataFrame.from_records(l_investimentos, index=investimentos.keys())
df_investimentos['Retorno'] = df_investimentos.apply(lambda l: l.valor * (1 + l.taxa) ** l.periodo, axis = 1)
print(df_investimentos)

df_investimentos.plot(kind = 'bar', y='Retorno', legend='nome')
plt.title('Retorno de Investimentos')
plt.xlabel('Investimentos')
plt.ylabel('Retorno Reais')
plt.show()