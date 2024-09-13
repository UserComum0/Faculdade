import os

peso = input('Digite seu peso: ')
altura = input('Digite sua altura: ')

altura_number = float(altura)
peso_number = float(peso)

os.system('cls')

imc = peso_number / (altura_number * altura_number)

if imc <= 18.5: 
    print(f'Seu IMC é de {imc} e você está Abaixo do peso')
elif imc > 18.5 and imc <= 24.9:
    print(f'Seu IMC é de {imc} e você está no Peso ideal')
elif imc > 25 and imc <= 29.9:
    print(f'Seu IMC é de {imc} e você está no Sobrepeso')
elif imc > 30 and imc <= 34.9:
    print(f'Seu IMC é de {imc} e você está na Obesidade grau 1')
elif imc > 35 and imc <= 39.9:
    print(f'Seu IMC é de {imc} e você está na Obesidade grau 2')
else:
    print(f'Seu IMC é de {imc} e você está na Obesidade grau 3')