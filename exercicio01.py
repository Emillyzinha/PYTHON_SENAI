lista = []

for i in range(0, 5):
    numeros = int(input("Digite o valor: "))
    lista.append(numeros)
    print(lista)
    lista.sort()
    maior = lista[4:]
    menor = lista[:1]
print(f"Em ordem descrescente: {lista}")
print(f"Maior valor: {maior}")
print(f"Menor valor: {menor}")