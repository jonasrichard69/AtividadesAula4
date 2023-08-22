jogos_jogadores = {'Futebol': 22, 'Vôlei': 12, 'Basquete': 10}
jogo = input('Digite o nome de um jogo: ')
jogadores = jogos_jogadores.get(jogo)
if jogadores:
    print('O jogo', jogo, 'precisa de', jogadores, 'jogadores')
else:
    print('Jogo não encontrado no dicionário')
