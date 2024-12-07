class Tarefa:
    def __init__(self, descricao, prioridade):
        self.descricao = descricao
        self.prioridade = prioridade

class GerenciadorTarefas:
    def __init__(self):
        self.tarefas = []

    def adicionar_tarefa(self, tarefa):
        self.tarefas.append(tarefa)

    def listar_tarefas(self):
        for i, tarefa in enumerate(self.tarefas, start=1):
            print(f"{i}. Descrição: {tarefa.descricao}, Prioridade: {tarefa.prioridade}")

if __name__ == "__main__":
    gerenciador = GerenciadorTarefas()

    while True:
        print("\n1. Adicionar Tarefa")
        print("2. Listar Tarefas")
        print("3. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            descricao = input("Digite a descrição da tarefa: ")
            prioridade = input("Digite a prioridade da tarefa: ")
            tarefa = Tarefa(descricao, prioridade)
            gerenciador.adicionar_tarefa(tarefa)
        elif escolha == "2":
            print("Lista de Tarefas:")
            gerenciador.listar_tarefas()
        elif escolha == "3":
            print("Saindo do Gerenciador de Tarefas. Até a próxima!")
            break
        else:
            print("Opção inválida. Tente novamente.")