'''
Exercício:
Faça um programa que pergunte a idade, o peso e a altura de uma pessoa
e decide se ela está apta a ser do Exercito.
Para entrar no exercito é preciso ter mais de 18 anos
e pesar mais ou igual a 60 kilos e medir mais ou igual a 1,70 metros
'''

print('Vamos saber se você está apto para ir ao exercito?')
idade = int(input('Informe sua idade: '))
peso = float(input('Informe seu peso:'))
altura = float(input('Informe sua altura: '))

if (idade <= 18) and (peso >= 60.0) and (altura >= 1.70):
    print("Você está apto para ir ao exercito")
else:
    print("Infelizmente você não está apto")