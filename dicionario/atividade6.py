alimentos_calorias = {'Maçã': 52, 'Banana': 89, 'Pão francês': 150}
alimento = input('Digite o nome de um alimento: ')
calorias = alimentos_calorias.get(alimento)
if calorias:
    print('O alimento', alimento, 'tem', calorias, 'calorias')
else:
    print('Alimento não encontrado no dicionário')
