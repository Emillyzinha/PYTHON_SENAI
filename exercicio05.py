lista1 = []
lista2 = []
lista3 = []

for i in range(0, 5):
    numeros = int(input("Digite um número: "))
    lista1.append(numeros)
    lista1.sort()
    if numeros %2 == 0:
        lista2.append(numeros)
        lista2.sort()
    else:
        lista3.append(numeros)
        lista3.sort()

print("Todos os valores: ", lista1)
print("Valores pares: ", lista2)
print("Valores ímpares: ",lista3)


# y = 2
# x = 5
#
# y, x = x, y
#
# print (y)
# print(x)