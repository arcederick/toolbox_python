class ContaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.__titular = titular  # Atributo privado
        self.__saldo = saldo_inicial  # Atributo privado

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f"Depósito de R${valor} realizado. Novo saldo: R${self.__saldo}")
        else:
            print("Valor inválido para depósito.")

    def sacar(self, valor):
        if valor > 0 and valor <= self.__saldo:
            self.__saldo -= valor
            print(f"Saque de R${valor} realizado. Novo saldo: R${self.__saldo}")
        else:
            print("Saque não autorizado. Saldo insuficiente ou valor inválido.")

    def consultar_saldo(self):
        print(f"Saldo atual de {self.__titular}: R${self.__saldo}")

    def alterar_titular(self, novo_titular):
        self.__titular = novo_titular
        print(f"Titular da conta alterado para: {self.__titular}")

if __name__ == "__main__":
    conta = ContaBancaria("João", 1000.0)

    conta.consultar_saldo()
    conta.depositar(500.0)
    conta.sacar(200.0)
    conta.consultar_saldo()

    # Tentativa de acesso direto aos atributos privados (não deve funcionar)
    # print(conta.__saldo)  # Isso causará um erro de atributo