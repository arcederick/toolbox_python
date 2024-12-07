class Tarefa:
    def __init__(self, descricao, prioridade):
        self.descricao = descricao
        self.prioridade = prioridade

class GerenciadorDeTarefas:
    def __init__(self):
        self.tarefas = []

    def adicionar_tarefa(self, descricao, prioridade):
        tarefa = Tarefa(descricao, prioridade)
        self.tarefas.append(tarefa)

    def listar_tarefas(self):
        for i, tarefa in enumerate(self.tarefas, start=1):
            print(f"{i}. Descrição: {tarefa.descricao}, Prioridade: {tarefa.prioridade}")

    def marcar_concluida(self, indice):
        if 1 <= indice <= len(self.tarefas):
            self.tarefas.pop(indice - 1)
            print("Tarefa marcada como concluída.")
        else:
            print("Índice inválido.")

gerenciador = GerenciadorDeTarefas()

while True:
    print("Aplicativo de Gerenciamento de Tarefas")
    print("1. Adicionar Tarefa")
    print("2. Listar Tarefas")
    print("3. Marcar Tarefa como Concluída")
    print("4. Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        descricao = input("Digite a descrição da tarefa: ")
        prioridade = input("Digite a prioridade da tarefa: ")
        gerenciador.adicionar_tarefa(descricao, prioridade)
        print("Tarefa adicionada com sucesso!")
    elif escolha == "2":
        gerenciador.listar_tarefas()
    elif escolha == "3":
        indice = int(input("Digite o número da tarefa concluída: "))
        gerenciador.marcar_concluida(indice)
    elif escolha == "4":
        break
    else:
        print("Opção inválida. Tente novamente.")