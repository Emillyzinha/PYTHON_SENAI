# import random
# n = 0
# print("-----------------------------------")
# print("             MEGA SENA             ")
# print("-----------------------------------")
# jogo = int(input("Quantos jogos deseja? "))
# print("-----------  Sorteando", jogo,"jogos")
#
# while jogo != 0:
#     x = random.sample(range(60), 6)
#     jogo-=1
#     n+=1
#     print("Jogo", n,":", x)
import random

qtd = int(input("Quantos jogos deseja? "))

lista = []

contador = 1

while True:
    lista.clear()
    while len(lista) != 6:
        auxiliar = random.randint(1, 60)
        if auxiliar not in lista:
            lista.append(auxiliar)
    print(f"O jogo {contador} é: {lista}")
    contador += 1
    if contador > qtd:
        break