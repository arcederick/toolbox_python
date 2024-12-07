class FinancasPessoais:
    def __init__(self):
        self.saldo = 0.0

    def adicionar_receita(self, valor):
        self.saldo += valor
        print(f"Receita de R${valor} adicionada. Saldo atual: R${self.saldo:.2f}")

    def adicionar_despesa(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"Despesa de R${valor} adicionada. Saldo atual: R${self.saldo:.2f}")
        else:
            print("Saldo insuficiente para adicionar a despesa.")

    def verificar_saldo(self):
        print(f"Saldo atual: R${self.saldo:.2f}")

financas = FinancasPessoais()

while True:
    print("Gerenciador de Finanças Pessoais")
    print("1. Adicionar Receita")
    print("2. Adicionar Despesa")
    print("3. Verificar Saldo")
    print("4. Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        valor = float(input("Digite o valor da receita: "))
        financas.adicionar_receita(valor)
    elif escolha == "2":
        valor = float(input("Digite o valor da despesa: "))
        financas.adicionar_despesa(valor)
    elif escolha == "3":
        financas.verificar_saldo()
    elif escolha == "4":
        break
    else:
        print("Opção inválida. Tente novamente.")