'''
Exercício
Faça um programa que leia a quantidade de pessoas que serão convidadas
para uma festa. Ápos isso o programa irá perguntar o nome de todas as
pessoas e colocar em uma lista de convidados.
Após isso imprimir todos os nomes da lista.
'''

quantidadePessoas = int(input('Quantas pessoas serão convidadas?'))
listaConvidados = []

while quantidadePessoas != 0:
    convidado = input('Digite o nome do convidado: ')
    listaConvidados.append(convidado)
    quantidadePessoas -= 1

print("Convidados:")
for nome in listaConvidados:
    print(nome)