notas = set([8, 7, 9, 6])
media = sum(notas) / len(notas)
if media >= 7:
    print('O aluno foi aprovado com média', media)
else:
    print('O aluno foi reprovado com média', media)
