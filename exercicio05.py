lista1 = []
lista2 = []
lista3 = []

for i in range(0, 5):
    numeros = int(input("Digite um número: "))
    lista1.append(numeros)
    if numeros %2 == 0:
        lista2.append(numeros)
        lista1.sort()
        print("Todos os valores: ", lista1)
        print("Valores pares: ", lista2)
    else:
        lista3.append(numeros)
        print("Valores ímpares: ",lista3)