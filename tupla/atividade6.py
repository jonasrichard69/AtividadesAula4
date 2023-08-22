cores_arco_iris = ('Vermelho', 'Laranja', 'Amarelo', 'Verde', 'Azul', 'Anil', 'Violeta')
cor = input('Digite uma cor: ')
if cor in cores_arco_iris:
    print('A cor', cor, 'está presente no arco-íris')
else:
    print('A cor', cor, 'não está presente no arco-íris')
