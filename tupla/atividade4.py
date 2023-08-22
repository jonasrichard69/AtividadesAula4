pessoas = ('João', 'Maria', 'José', 'Ana', 'Carlos')
numero = int(input('Digite um número entre 1 e 5: '))
if 1 <= numero <= 5:
    nome = pessoas[numero - 1]
    print('O nome correspondente ao número digitado é:', nome)
else:
    print('Número inválido')
