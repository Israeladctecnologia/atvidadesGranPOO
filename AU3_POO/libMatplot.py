import matplotlib.pyplot as plt

'''
meses = ['jan','fev','mar','abr','mai','jun']
qtdTI = [60, 52, 71, 82, 105, 72]
qtdRh = [40, 20, 80, 60, 80,50]

plt.plot(meses, qtdTI, label='TI', color= 'blue', marker='.')
plt.plot(meses, qtdRh, label='Rh', color= 'red', marker='.')
plt.title('Chamados abertos')
plt.xlabel('meses')
plt.ylabel('quantidade')
plt.legend()

plt.show()
'''

navegadores = ['chrome', 'firefox', 'edge']
quantidade = [1200, 800, 400]

plt.pie(quantidade, labels=navegadores)

plt.show()

