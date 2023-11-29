import pandas as pd

cidades = [
    {'nome':'Distrito Federal', 'uf':'DF', 'populacao':'5000000'},
    {'nome':'São Paulo', 'uf':'SP', 'populacao':'11000000'},
    {'nome':'Rio de Janeiro', 'uf':'RJ', 'populacao':'4000000'},
    {'nome':'Florianopoli', 'uf':'SC', 'populacao':'1000000'},
    {'nome':'Curitiba', 'uf':'PR', 'populacao':'1500000'},
]

dataFrame = pd.DataFrame(cidades)
ordenado = dataFrame.sort_values(by='populacao', ascending=False)
print(ordenado)
print()
print(ordenado.head(2)['nome'])
