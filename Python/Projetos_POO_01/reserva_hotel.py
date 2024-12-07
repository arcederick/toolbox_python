class Quarto:
    def __init__(self, numero, tipo, ocupado=False):
        self.numero = numero
        self.tipo = tipo
        self.ocupado = ocupado

class Hotel:
    def __init__(self, nome, total_quartos):
        self.nome = nome
        self.quartos = [Quarto(numero=i, tipo="Simples") for i in range(1, total_quartos + 1)]

    def listar_quartos_disponiveis(self):
        print("Quartos Disponíveis:")
        for quarto in self.quartos:
            if not quarto.ocupado:
                print(f"Número: {quarto.numero}, Tipo: {quarto.tipo}")

    def reservar_quarto(self, numero_quarto):
        quarto = self.encontrar_quarto(numero_quarto)
        if quarto:
            if not quarto.ocupado:
                quarto.ocupado = True
                print(f"Quarto {quarto.numero} reservado com sucesso.")
            else:
                print(f"Quarto {quarto.numero} já está ocupado.")
        else:
            print("Quarto não encontrado.")

    def encontrar_quarto(self, numero_quarto):
        for quarto in self.quartos:
            if quarto.numero == numero_quarto:
                return quarto
        return None

hotel = Hotel(nome="Hotel Python", total_quartos=10)

while True:
    print("Sistema de Reservas de Hotel")
    print("1. Listar Quartos Disponíveis")
    print("2. Reservar Quarto")
    print("3. Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        hotel.listar_quartos_disponiveis()
    elif escolha == "2":
        numero_quarto = int(input("Digite o número do quarto a ser reservado: "))
        hotel.reservar_quarto(numero_quarto)
    elif escolha == "3":
        break
    else:
        print("Opção inválida. Tente novamente.")