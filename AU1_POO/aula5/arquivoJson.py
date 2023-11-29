import  json

pessoas = [
    {'nome':'Israel', 'tell':'43 9988-6644', 'end':'Pr'},
    {'nome':'GIovana', 'tell':'43 9977-2674', 'end':'Pr'},
    {'nome':'Deza', 'tell':'43 4875-3589', 'end':'To'},
]
with open('pessoas.json', 'w') as arquivo:
    json.dump(pessoas, arquivo)