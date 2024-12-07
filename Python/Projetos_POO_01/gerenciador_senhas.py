import hashlib

class GerenciadorDeSenhas:
    def __init__(self):
        self.senhas = {}

    def adicionar_senha(self, website, username, senha):
        hash_senha = hashlib.sha256(senha.encode()).hexdigest()
        self.senhas[website] = {"username": username, "senha": hash_senha}

    def recuperar_senha(self, website, senha_digitada):
        if website in self.senhas:
            hash_senha = hashlib.sha256(senha_digitada.encode()).hexdigest()
            if hash_senha == self.senhas[website]["senha"]:
                return self.senhas[website]["username"]
        return None

gerenciador = GerenciadorDeSenhas()

while True:
    print("Gerenciador de Senhas")
    print("1. Adicionar Senha")
    print("2. Recuperar Senha")
    print("3. Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        website = input("Digite o nome do website: ")
        username = input("Digite o nome de usuário: ")
        senha = input("Digite a senha: ")
        gerenciador.adicionar_senha(website, username, senha)
        print("Senha adicionada com sucesso!")
    elif escolha == "2":
        website = input("Digite o nome do website: ")
        senha_digitada = input("Digite a senha: ")
        username = gerenciador.recuperar_senha(website, senha_digitada)
        if username:
            print(f"Nome de usuário: {username}")
        else:
            print("Senha incorreta ou website não encontrado.")
    elif escolha == "3":
        break
    else:
        print("Opção inválida. Tente novamente.")