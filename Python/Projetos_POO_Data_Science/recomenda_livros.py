import random

class Livro:
    def __init__(self, titulo, autor, genero):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero

class Usuario:
    def __init__(self, nome):
        self.nome = nome
        self.livros_lidos = []

    def ler_livro(self, livro):
        self.livros_lidos.append(livro)

    def recomendar_livro(self, biblioteca):
        livros_nao_lidos = [livro for livro in biblioteca if livro not in self.livros_lidos]
        if not livros_nao_lidos:
            return "Você já leu todos os livros disponíveis."
        livro_recomendado = random.choice(livros_nao_lidos)
        return f"Recomendação para {self.nome}: '{livro_recomendado.titulo}' por {livro_recomendado.autor}"

if __name__ == "__main__":
    biblioteca_livros = [
        Livro("Dom Quixote", "Miguel de Cervantes", "Ficção"),
        Livro("Cem Anos de Solidão", "Gabriel García Márquez", "Ficção"),
        Livro("A Revolução dos Bichos", "George Orwell", "Ficção"),
    ]

    usuario1 = Usuario("Alice")
    usuario1.ler_livro(biblioteca_livros[0])

    recomendacao = usuario1.recomendar_livro(biblioteca_livros)
    print(recomendacao)