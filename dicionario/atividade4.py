estados_capitais = {'São Paulo': 'São Paulo', 'Rio de Janeiro': 'Rio de Janeiro', 'Minas Gerais': 'Belo Horizonte'}
estado = input('Digite o nome de um estado: ')
capital = estados_capitais.get(estado)
if capital:
    print('A capital do estado', estado, 'é', capital)
else:
    print('Estado não encontrado no dicionário')
