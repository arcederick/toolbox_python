class Projeto:
    def __init__(self, nome, descricao, prazo):
        self.nome = nome
        self.descricao = descricao
        self.prazo = prazo
        self.tarefas = []

    def adicionar_tarefa(self, tarefa):
        self.tarefas.append(tarefa)

    def listar_tarefas(self):
        for tarefa in self.tarefas:
            print(f"Tarefa: {tarefa}")

class GerenciadorDeProjetos:
    def __init__(self):
        self.projetos = []

    def adicionar_projeto(self, nome, descricao, prazo):
        projeto = Projeto(nome, descricao, prazo)
        self.projetos.append(projeto)

    def listar_projetos(self):
        for projeto in self.projetos:
            print(f"Projeto: {projeto.nome}, Prazo: {projeto.prazo}")
            print(f"Descrição: {projeto.descricao}\nTarefas:")

            if projeto.tarefas:
                for tarefa in projeto.tarefas:
                    print(f"  - {tarefa}")
            else:
                print("  - Nenhuma tarefa definida")

gerenciador = GerenciadorDeProjetos()

while True:
    print("Sistema de Gerenciamento de Projetos")
    print("1. Adicionar Projeto")
    print("2. Listar Projetos")
    print("3. Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        nome = input("Digite o nome do projeto: ")
        descricao = input("Digite a descrição do projeto: ")
        prazo = input("Digite o prazo do projeto: ")
        gerenciador.adicionar_projeto(nome, descricao, prazo)
        print("Projeto adicionado com sucesso!")
    elif escolha == "2":
        gerenciador.listar_projetos()
    elif escolha == "3":
        break
    else:
        print("Opção inválida. Tente novamente.")