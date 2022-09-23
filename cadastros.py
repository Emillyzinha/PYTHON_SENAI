import random


def menu():
    print("\n[1] Adicionar Usuário\n"
          "[2] Listar Usuários\n"
          "[3] Pesquisar Usuário\n"
          "[4] Atualizar Usuário\n"
          "[5] Para sair\n")


def adicionar_cadastro(n):
    dicionario = {"NOME": "", "IDADE": "", "CEP": ""}
    matricula1 = random.randint(0, 50)
    if n == 1:
        for i, cad in enumerate(dicionario):
            cadastro = input(f"Digite o seu {cad}: ")
            dicionario[cad] = cadastro
        print(f"A sua matrícula é: {matricula1}")
        dicionario["Matricula"] = matricula1
        lista.append(dicionario.copy())
    # print(lista)


def listar_usuario():
    if opcao == 2:
        print(lista)


def pesquisar_ususario():
    if opcao == 3:
        encontrou = False
        matricula = int(input("Digite o número da sua matícula: "))
        for indice1, lista_completa in enumerate(lista):
            for indice2, itens in enumerate(lista_completa):
                if matricula == lista_completa[itens]:
                    encontrou = True
                    print(lista_completa)
        if encontrou == False:
            print(f"A matrícula {matricula} não existe")


def atualizar_usuario():
    if opcao == 4:
        encontrou = False
        matricula = int(input("Digite sua matrícula para identificação, por favor: "))
        for index1, lista_completa in enumerate(lista):
            for index2, item_dicionario in enumerate(lista_completa):
                if matricula == lista_completa[item_dicionario]:
                    encontrou = True
                    print(f'Encontrou no index {index1} - {index2}')
                    atualizar_salvando(lista_completa, index1)


def atualizar_salvando(registro, indexLista):
    print(registro)
    campo_atualizar = input("Escreva o campo que você quer atualizar? ").upper()
    for i, chave in enumerate(registro):
        if campo_atualizar == chave:
            campo_atualizado = input(f"Escreva seu/sua {chave}: ")
            registro[chave] = campo_atualizado
            print(registro)
            lista.pop(indexLista)
            lista.append(registro)

if __name__ == '__main__':
    matricula1 = random.sample(range(1, 100), 1)
    dicionario = {"NOME": "", "IDADE": "", "CEP": ""}
    lista = []
    while True:
        menu()
        opcao = int(input("Escolha a opção desejada: "))
        if opcao == 5:
            break
        adicionar_cadastro(opcao)
        listar_usuario()
        pesquisar_ususario()
        atualizar_usuario()
