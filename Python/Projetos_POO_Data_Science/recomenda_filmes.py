import random

class Filme:
    def __init__(self, titulo, genero):
        self.titulo = titulo
        self.genero = genero

class Usuario:
    def __init__(self, nome):
        self.nome = nome
        self.avaliacoes = {}

    def avaliar_filme(self, filme, nota):
        self.avaliacoes[filme.titulo] = nota

    def recomendar_filme(self, filmes):
        filmes_nao_vistos = [filme for filme in filmes if filme.titulo not in self.avaliacoes]
        if not filmes_nao_vistos:
            return "Você já assistiu a todos os filmes disponíveis."
        filme_recomendado = random.choice(filmes_nao_vistos)
        return f"Recomendação para {self.nome}: {filme_recomendado.titulo} ({filme_recomendado.genero})"

if __name__ == "__main__":
    # Crie alguns filmes e um usuário
    filme1 = Filme("Matrix", "Ação")
    filme2 = Filme("O Poderoso Chefão", "Crime")
    filme3 = Filme("Star Wars", "Ficção Científica")
    usuario1 = Usuario("Alice")

    # O usuário avalia os filmes
    usuario1.avaliar_filme(filme1, 4.5)
    usuario1.avaliar_filme(filme2, 5.0)

    # Recomendar um filme ao usuário
    filmes_disponiveis = [filme1, filme2, filme3]
    recomendacao = usuario1.recomendar_filme(filmes_disponiveis)
    print(recomendacao)