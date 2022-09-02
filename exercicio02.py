lista = []

print("Digite qualquer letra para encerrar")
while True:
    numeros = int(input("Digite um número: "))
    if numeros not in lista:
        lista.append(numeros)
    else:
        break

lista.sort()
print(lista)