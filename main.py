import time

def program():
    dic = {}
    lista = []

    while True:
        campo = input("Digite o nome do campo desejado: ")
        if campo == "":
            break
        else:
            dic[campo] = ""
            continue
    print("Adicionando dados...")
    time.sleep(5)
    while True:
        for x, y in enumerate(dic):
            campo2 = input(f"Por favor, digite o {y}: ")
            dic[y] = campo2
        lista.append(dic.copy())
        cont = input("Digite enter para continuar e qualquer letra para sair: ")
        if cont != "":
            break
    print(lista)


if __name__=="__main__":
    program()