class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True

class Biblioteca:
    def __init__(self):
        self.catalogo = []

    def adicionar_livro(self, titulo, autor):
        livro = Livro(titulo, autor)
        self.catalogo.append(livro)

    def listar_livros(self):
        for livro in self.catalogo:
            status = "Disponível" if livro.disponivel else "Indisponível"
            print(f"Título: {livro.titulo}, Autor: {livro.autor}, Status: {status}")

    def emprestar_livro(self, titulo):
        for livro in self.catalogo:
            if livro.titulo == titulo:
                if livro.disponivel:
                    livro.disponivel = False
                    print(f"Empréstimo de '{titulo}' realizado com sucesso.")
                else:
                    print(f"'{titulo}' não está disponível no momento.")
                return
        print(f"'{titulo}' não encontrado na biblioteca.")

    def devolver_livro(self, titulo):
        for livro in self.catalogo:
            if livro.titulo == titulo:
                livro.disponivel = True
                print(f"'{titulo}' devolvido com sucesso.")
                return
        print(f"'{titulo}' não encontrado na biblioteca.")

biblioteca = Biblioteca()

while True:
    print("Sistema de Gerenciamento de Biblioteca")
    print("1. Adicionar Livro")
    print("2. Listar Livros")
    print("3. Emprestar Livro")
    print("4. Devolver Livro")
    print("5. Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        titulo = input("Digite o título do livro: ")
        autor = input("Digite o autor do livro: ")
        biblioteca.adicionar_livro(titulo, autor)
        print("Livro adicionado com sucesso!")
    elif escolha == "2":
        biblioteca.listar_livros()
    elif escolha == "3":
        titulo = input("Digite o título do livro a ser emprestado: ")
        biblioteca.emprestar_livro(titulo)
    elif escolha == "4":
        titulo = input("Digite o título do livro a ser devolvido: ")
        biblioteca.devolver_livro(titulo)
    elif escolha == "5":
        break
    else:
        print("Opção inválida. Tente novamente.")