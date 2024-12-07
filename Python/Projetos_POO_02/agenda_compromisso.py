class Compromisso:
    def __init__(self, data, hora, descricao):
        self.data = data
        self.hora = hora
        self.descricao = descricao

class Agenda:
    def __init__(self):
        self.compromissos = []

    def adicionar_compromisso(self, data, hora, descricao):
        compromisso = Compromisso(data, hora, descricao)
        self.compromissos.append(compromisso)

    def listar_compromissos(self):
        for i, compromisso in enumerate(self.compromissos, start=1):
            print(f"{i}. Data: {compromisso.data}, Hora: {compromisso.hora}, Descrição: {compromisso.descricao}")

agenda = Agenda()

while True:
    print("Agenda de Compromissos")
    print("1. Adicionar Compromisso")
    print("2. Listar Compromissos")
    print("3. Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        data = input("Digite a data (DD/MM/AAAA): ")
        hora = input("Digite a hora (HH:MM): ")
        descricao = input("Digite a descrição do compromisso: ")
        agenda.adicionar_compromisso(data, hora, descricao)
        print("Compromisso adicionado com sucesso!")
    elif escolha == "2":
        agenda.listar_compromissos()
    elif escolha == "3":
        break
    else:
        print("Opção inválida. Tente novamente.")