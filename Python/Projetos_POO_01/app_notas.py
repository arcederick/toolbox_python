class Nota:
    def __init__(self, titulo, conteudo):
        self.titulo = titulo
        self.conteudo = conteudo

class AplicativoDeNotas:
    def __init__(self):
        self.notas = []

    def adicionar_nota(self, titulo, conteudo):
        nota = Nota(titulo, conteudo)
        self.notas.append(nota)

    def editar_nota(self, titulo, novo_conteudo):
        for nota in self.notas:
            if nota.titulo == titulo:
                nota.conteudo = novo_conteudo
                return True
        return False

    def excluir_nota(self, titulo):
        for nota in self.notas:
            if nota.titulo == titulo:
                self.notas.remove(nota)
                return True
        return False

    def listar_notas(self):
        for nota in self.notas:
            print(f"--- {nota.titulo} ---\n{nota.conteudo}\n")

app = AplicativoDeNotas()

while True:
    print("Aplicativo de Notas")
    print("1. Adicionar Nota")
    print("2. Editar Nota")
    print("3. Excluir Nota")
    print("4. Listar Notas")
    print("5. Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        titulo = input("Digite o título da nota: ")
        conteudo = input("Digite o conteúdo da nota: ")
        app.adicionar_nota(titulo, conteudo)
        print("Nota adicionada com sucesso!")
    elif escolha == "2":
        titulo = input("Digite o título da nota a ser editada: ")
        novo_conteudo = input("Digite o novo conteúdo da nota: ")
        if app.editar_nota(titulo, novo_conteudo):
            print("Nota editada com sucesso!")
        else:
            print("Nota não encontrada.")
    elif escolha == "3":
        titulo = input("Digite o título da nota a ser excluída: ")
        if app.excluir_nota(titulo):
            print("Nota excluída com sucesso!")
        else:
            print("Nota não encontrada.")
    elif escolha == "4":
        app.listar_notas()
    elif escolha == "5":
        break
    else:
        print("Opção inválida. Tente novamente.")