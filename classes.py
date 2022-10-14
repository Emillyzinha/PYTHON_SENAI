import time

class Veiculo:
    def __init__(self, marca, modelo, placa, consumo, nivel_combustivel):
        self.marca = marca
        self.modelo = modelo
        self.placa = placa
        self.consumo = consumo
        self.nivel_combustvel = nivel_combustivel

class Carro(Veiculo) :
    saldo = 100
    def __init__(self, marca, modelo, placa, consumo, nivel_combustivel, categoria, airbgs, litros_por_mala, conversivel):
        super().__init__(marca, modelo, placa, consumo, nivel_combustivel)
        self.categoria = categoria
        self.airbgs = airbgs
        self.litros_por_mala = litros_por_mala
        self.conversivel = conversivel

    def acelerar(self):
        if Status.velocidade >= 110:
            print("Limite da rodovia: 110km/h.")
        else:
            Status.velocidade += 50
            print('-'* 40)
            print("Você está acelerando 10Km/h.")
            print(f"Sua velocidade está em: {Status.velocidade}Km/h.")
            IA.velocidade = Status.velocidade

    def desacelerar(self):
        Status.velocidade -= 10
        if Status.velocidade <= 0:
            print('-' * 40)
            print('            Você está parado')
            IA.running = False
        else:
            print('-'* 40)
            print("Você está desacelerando 10Km/h.")
            print(f"Sua velocidade está em: {Status.velocidade}Km/h.")

    def carteira(self):
        IA.running = False
        print(f"Seu saldo é: {Carro.saldo}")
        print("-----------------------\n"
              "[1] Sacar\n"
              "[2] Depositar")
        desejo = int(input("Digite a opcão desejada: "))
        if desejo == 1:
            valorSaque = int(input("Qual o valor deseja sacar? "))
            while valorSaque > Carro.saldo:
                print("Você não tem saldo o suficiente")
                return valorSaque
            Carro.saldo -=valorSaque
            print(Carro.saldo)
        if desejo == 2:
            valorDeposito = int(input("Digite o valor do deposito: "))
            while valorDeposito <= 0:
                print("Digite um deposito válido, acima de 0")
                return valorDeposito
            Carro.saldo+=valorDeposito
            print(Carro.saldo)

class Status:
    movimento = False
    distancia = 0
    velocidade = 10
    def __init__(self):
        pass
    def rodou(self, velocidade, distancia):
        while distancia > 0:
            rodados = velocidade * 0.1
            distancia -= rodados
            #tempo+=1
            print("-"*30)
            print(f"Você está a {distancia}km/h do seu destino.")
            time.sleep(5)

class IA:
    running = False
    distancia = 0
    velocidade = 0

class Exibir:
    def atualizar(self):
        while True:
            rodados = IA.velocidade * 0.1
            IA.distancia -= rodados
            tempo = IA.distancia/IA.velocidade * 2
            print(f"\nVocê está a {IA.distancia}km/h e {tempo} minutos do seu destino.")
            time.sleep(0.1)

            if not IA.running:
                break
            if IA.distancia <= 0:
                print(f'\nVocê chegou ao seu destino!')
                IA.velocidade = 0
                IA.running = False
                break

