from sklearn.cluster import KMeans
import numpy as np

class Produto:
    def __init__(self, nome, preco, peso):
        self.nome = nome
        self.preco = preco
        self.peso = peso

produtos = [
    Produto('Produto 1', 60.50, 0.50),
    Produto('Produto 2', 25, 0.50),
    Produto('Produto 3', 30, 0.9),
    Produto('Produto 4', 32.50, 0.38),
    Produto('Produto 5', 54.70, 1.3),
    Produto('Produto 6', 15.50, 0.3),
]

preco = [[p.preco, p.peso] for p in produtos]
matriz = np.array(preco)

kmeans = KMeans(n_init='auto', n_clusters=2, random_state=0).fit(matriz)
labels = kmeans.labels_

for i in range(2):
    print(f"Grpo {i+1}:")
    for j in range(len(produtos)):
        if labels[j] == i:
            print('-', produtos[j].nome)