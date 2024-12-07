class Aviao:
    def __init__(self, modelo):
        self.modelo = modelo
        self.altitude = 0
        self.velocidade = 0
        self.status_motor = False

    def ligar_motor(self):
        self.status_motor = True
        print("Motor ligado.")

    def desligar_motor(self):
        self.status_motor = False
        print("Motor desligado.")

    def decolar(self):
        if self.status_motor:
            self.velocidade = 250
            self.altitude = 10000
            print("Avião decolou.")
        else:
            print("Ligue o motor antes de decolar.")

    def pousar(self):
        self.velocidade = 0
        self.altitude = 0
        print("Avião pousou.")

    def aumentar_altitude(self, metros):
        if self.status_motor:
            self.altitude += metros
            print(f"Altitude aumentada para {self.altitude} metros.")
        else:
            print("Ligue o motor para aumentar a altitude.")

    def diminuir_altitude(self, metros):
        if self.status_motor:
            self.altitude -= metros
            print(f"Altitude diminuída para {self.altitude} metros.")
        else:
            print("Ligue o motor para diminuir a altitude.")

    def aumentar_velocidade(self, kmh):
        if self.status_motor:
            self.velocidade += kmh
            print(f"Velocidade aumentada para {self.velocidade} km/h.")
        else:
            print("Ligue o motor para aumentar a velocidade.")

    def diminuir_velocidade(self, kmh):
        if self.status_motor:
            self.velocidade -= kmh
            print(f"Velocidade diminuída para {self.velocidade} km/h.")
        else:
            print("Ligue o motor para diminuir a velocidade.")

    def status(self):
        print(f"Modelo: {self.modelo}")
        print(f"Altitude: {self.altitude} metros")
        print(f"Velocidade: {self.velocidade} km/h")
        print(f"Motor ligado: {self.status_motor}")

aviao = Aviao("Boeing 737")

while True:
    print("Simulador de Voo")
    print("1. Ligar Motor")
    print("2. Desligar Motor")
    print("3. Decolar")
    print("4. Pousar")
    print("5. Aumentar Altitude")
    print("6. Diminuir Altitude")
    print("7. Aumentar Velocidade")
    print("8. Diminuir Velocidade")
    print("9. Status do Avião")
    print("10. Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        aviao.ligar_motor()
    elif escolha == "2":
        aviao.desligar_motor()
    elif escolha == "3":
        aviao.decolar()
    elif escolha == "4":
        aviao.pousar()
    elif escolha == "5":
        metros = int(input("Digite a quantidade de metros para aumentar a altitude: "))
        aviao.aumentar_altitude(metros)
    elif escolha == "6":
        metros = int(input("Digite a quantidade de metros para diminuir a altitude: "))
        aviao.diminuir_altitude(metros)
    elif escolha == "7":
        kmh = int(input("Digite a quantidade de km/h para aumentar a velocidade: "))
        aviao.aumentar_velocidade(kmh)
    elif escolha == "8":
        kmh = int(input("Digite a quantidade de km/h para diminuir a velocidade: "))
        aviao.diminuir_velocidade(kmh)
    elif escolha == "9":
        aviao.status()
    elif escolha == "10":
        break
    else:
        print("Opção inválida. Tente novamente.")