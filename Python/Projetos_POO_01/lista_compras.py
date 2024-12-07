class ListaDeCompras:
    def __init__(self):
        self.itens = []

    def adicionar_item(self, item):
        self.itens.append(item)

    def remover_item(self, item):
        if item in self.itens:
            self.itens.remove(item)
        else:
            print("Item não encontrado na lista.")

    def listar_itens(self):
        print("Lista de Compras:")
        for item in self.itens:
            print(f"- {item}")

if __name__ == "__main__":
    lista = ListaDeCompras()

    while True:
        print("\n1. Adicionar Item")
        print("2. Remover Item")
        print("3. Listar Itens")
        print("4. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "4":
            print("Saindo do Aplicativo de Lista de Compras. Até a próxima!")
            break

        if escolha == "1":
            item = input("Digite o item a ser adicionado: ")
            lista.adicionar_item(item)
        elif escolha == "2":
            item = input("Digite o item a ser removido: ")
            lista.remover_item(item)
        elif escolha == "3":
            lista.listar_itens()
        else:
            print("Opção inválida. Tente novamente.")