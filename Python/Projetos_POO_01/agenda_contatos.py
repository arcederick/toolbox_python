class Contato:
    def __init__(self, nome, telefone, email):
        self.nome = nome
        self.telefone = telefone
        self.email = email

class AgendaDeContatos:
    def __init__(self):
        self.contatos = []

    def adicionar_contato(self, nome, telefone, email):
        contato = Contato(nome, telefone, email)
        self.contatos.append(contato)

    def editar_contato(self, nome, novo_telefone, novo_email):
        for contato in self.contatos:
            if contato.nome == nome:
                contato.telefone = novo_telefone
                contato.email = novo_email
                return True
        return False

    def excluir_contato(self, nome):
        for contato in self.contatos:
            if contato.nome == nome:
                self.contatos.remove(contato)
                return True
        return False

    def buscar_contato(self, nome):
        for contato in self.contatos:
            if contato.nome == nome:
                return contato
        return None

    def listar_contatos(self):
        for contato in self.contatos:
            print(f"Nome: {contato.nome}")
            print(f"Telefone: {contato.telefone}")
            print(f"Email: {contato.email}")
            print("")

agenda = AgendaDeContatos()

while True:
    print("Agenda de Contatos")
    print("1. Adicionar Contato")
    print("2. Editar Contato")
    print("3. Excluir Contato")
    print("4. Buscar Contato")
    print("5. Listar Contatos")
    print("6. Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        nome = input("Digite o nome do contato: ")
        telefone = input("Digite o telefone do contato: ")
        email = input("Digite o email do contato: ")
        agenda.adicionar_contato(nome, telefone, email)
        print("Contato adicionado com sucesso!")
    elif escolha == "2":
        nome = input("Digite o nome do contato a ser editado: ")
        novo_telefone = input("Digite o novo telefone: ")
        novo_email = input("Digite o novo email: ")
        if agenda.editar_contato(nome, novo_telefone, novo_email):
            print("Contato editado com sucesso!")
        else:
            print("Contato não encontrado.")
    elif escolha == "3":
        nome = input("Digite o nome do contato a ser excluído: ")
        if agenda.excluir_contato(nome):
            print("Contato excluído com sucesso!")
        else:
            print("Contato não encontrado.")
    elif escolha == "4":
        nome = input("Digite o nome do contato a ser buscado: ")
        contato = agenda.buscar_contato(nome)
        if contato:
            print(f"Nome: {contato.nome}")
            print(f"Telefone: {contato.telefone}")
            print(f"Email: {contato.email}")
        else:
            print("Contato não encontrado.")
    elif escolha == "5":
        agenda.listar_contatos()
    elif escolha == "6":
        break
    else:
        print("Opção inválida. Tente novamente.")