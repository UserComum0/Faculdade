alunos = []
num0 = []
num1 = []
num2 = []
num3 = []

for i in range(4):
    alunos.append(input('Digite o nome do aluno: '))
    num0.append(input('Digite a Primeira nota do aluno: '))
    num1.append(input('Digite a Segunda nota do aluno: '))
    num2.append(input('Digite a Terceira nota do aluno: '))
    num3.append(input('Digite a Quarta nota do aluno: '))

print('Alunos  | Notas')

for a in range(4):
    print(f'{alunos[a]} |{num0[a]}|{num1[a]}|{num2[a]}|{num3[a]}|')