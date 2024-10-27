# Começo do Programa

prova1 = int(input('Digite a nota da Primeira Prova: '))
# Pedir nota da primeira prova para declarar a variável (Prova 1)

prova2 = int(input('Digite a nota da Segunda Prova: '))
# Pedir nota da segunda prova para declarar a variável (Prova 2)

media = (prova1 + prova2) / 2
#  Calcular a média 2 / (Prova1 + Prova2)
# guardar o resultado da conta na variável (media)

print(media)
# exibir na tela a média

if (media > 6):
    # se a media for menor do que 6

    print('aluno passou')
    
    # exibir na tela que o aluno não passou

else:
    # se a media for maior do que 6

    print('aluno não passou')

    # exibir na tela que o aluno passou


# fim do programa