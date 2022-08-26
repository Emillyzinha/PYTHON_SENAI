lista = []
for i in range(0, 5):
    numeros = int(input("Digite um número: "))
    if numeros not in lista:
        lista.append(numeros)
        lista.sort()
        print(lista)
