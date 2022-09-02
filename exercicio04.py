lista = []

for i in range(0, 6):
    numeros = int(input("Digite um número: "))
    lista.append(numeros)
    print(lista)
len(lista)
print(f"Foram digitdos {len} números")
lista.sort(reverse=True)
print("Na forma decrescente: ", lista)
lista: list[int]
if 5 not in lista:
    print("O valor 5 não apareceu na lista")
else:
    print("O valor 5 está na lista")