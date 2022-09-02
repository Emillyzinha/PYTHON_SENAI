lista1 = []
lista2 = []
tamanho = len(lista1)

for i in range(0, 5):
    numero = int(input("Digite um valor: "))
    lista1.append(numero)

for i in range(0, tamanho):
    aux = min(lista1)
    lista2.append(aux)
    del lista1[lista1.index(aux)]

print(lista2)