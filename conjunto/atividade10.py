primos = set([2, 3, 5, 7, 11, 13, 17, 19])
numero = int(input('Digite um número: '))
if numero in primos:
    print('O número', numero, 'é primo e está no conjunto')
else:
    print('O número', numero, 'não é primo ou não está no conjunto')
