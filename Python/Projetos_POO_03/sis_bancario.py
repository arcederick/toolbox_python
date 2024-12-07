import random
import datetime

class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        self.contas = []

    def abrir_conta(self, tipo_conta, saldo_inicial):
        if tipo_conta == 'corrente':
            conta = ContaCorrente(saldo_inicial)
        elif tipo_conta == 'poupanca':
            conta = ContaPoupanca(saldo_inicial)
        else:
            raise ValueError("Tipo de conta inválido")
        
        self.contas.append(conta)
        return conta

    def __str__(self):
        return f"Cliente: {self.nome}, CPF: {self.cpf}"

class Conta:
    def __init__(self, saldo_inicial=0):
        self.numero_conta = random.randint(1000, 9999)
        self.saldo = saldo_inicial
        self.transacoes = []

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.registrar_transacao(f"Depósito de ${valor}")

    def sacar(self, valor):
        if valor > 0 and self.saldo >= valor:
            self.saldo -= valor
            self.registrar_transacao(f"Saque de ${valor}")

    def registrar_transacao(self, descricao):
        data_hora = datetime.datetime.now()
        self.transacoes.append((data_hora, descricao))

    def extrato(self):
        print(f"Extrato da Conta {self.numero_conta}")
        for data_hora, descricao in self.transacoes:
            print(f"{data_hora}: {descricao}")
        print(f"Saldo atual: ${self.saldo}")

class ContaCorrente(Conta):
    def __init__(self, saldo_inicial=0):
        super().__init__(saldo_inicial)
        self.tipo = 'corrente'

    def __str__(self):
        return f"Conta Corrente - Número: {self.numero_conta}, Saldo: ${self.saldo}"

class ContaPoupanca(Conta):
    def __init__(self, saldo_inicial=0):
        super().__init__(saldo_inicial)
        self.tipo = 'poupanca'
        self.taxa_juros = 0.03

    def calcular_juros(self):
        juros = self.saldo * self.taxa_juros
        self.saldo += juros
        self.registrar_transacao(f"Crédito de juros de ${juros}")

    def __str__(self):
        return f"Conta Poupança - Número: {self.numero_conta}, Saldo: ${self.saldo}"

if __name__ == "__main__":
    cliente1 = Cliente("João Silva", "123.456.789-00")
    conta_corrente = cliente1.abrir_conta("corrente", 1000)
    conta_poupanca = cliente1.abrir_conta("poupanca", 5000)

    cliente2 = Cliente("Maria Santos", "987.654.321-00")
    conta_corrente2 = cliente2.abrir_conta("corrente", 2000)

    # Realizar algumas operações
    conta_corrente.depositar(500)
    conta_poupanca.sacar(1000)
    conta_poupanca.calcular_juros()
    
    # Exibir extratos
    conta_corrente.extrato()
    conta_poupanca.extrato()
    conta_corrente2.extrato()