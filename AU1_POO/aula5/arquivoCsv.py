import csv

carros = [
    ['Vw', 'virtus', '2017'],
    ['Jeep', 'Compass','2022'],
    ['Toyota', 'Corola', '2023'],
]

with open('carros.csv','w', newline='') as arquivo:
    fileCSV = csv.writer(arquivo, delimiter=";")
    
    fileCSV.writerows(['Marca', 'modelo', 'ano'])
    fileCSV.writerows(carros)