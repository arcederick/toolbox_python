class Noticia:
    def __init__(self, titulo, conteudo):
        self.titulo = titulo
        self.conteudo = conteudo

class AplicativoDeNoticias:
    def __init__(self):
        self.noticias = []

    def adicionar_noticia(self, titulo, conteudo):
        noticia = Noticia(titulo, conteudo)
        self.noticias.append(noticia)

    def listar_noticias(self):
        for i, noticia in enumerate(self.noticias, start=1):
            print(f"{i}. Título: {noticia.titulo}")
            print(f"   Conteúdo: {noticia.conteudo}\n")

aplicativo = AplicativoDeNoticias()

while True:
    print("Aplicativo de Notícias")
    print("1. Adicionar Notícia")
    print("2. Listar Notícias")
    print("3. Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        titulo = input("Digite o título da notícia: ")
        conteudo = input("Digite o conteúdo da notícia: ")
        aplicativo.adicionar_noticia(titulo, conteudo)
        print("Notícia adicionada com sucesso!")
    elif escolha == "2":
        aplicativo.listar_noticias()
    elif escolha == "3":
        break
    else:
        print("Opção inválida. Tente novamente.")