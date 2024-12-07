class Funcionario:
    def __init__(self, nome, cargo, salario):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario
        self.horas_trabalhadas = []

    def registrar_entrada(self, hora):
        self.horas_trabalhadas.append((hora, "entrada"))

    def registrar_saida(self, hora):
        self.horas_trabalhadas.append((hora, "saída"))

    def calcular_horas_trabalhadas(self):
        entradas = [hora for hora, acao in self.horas_trabalhadas if acao == "entrada"]
        saidas = [hora for hora, acao in self.horas_trabalhadas if acao == "saída"]
        
        if len(entradas) == len(saidas):
            total_horas = sum([(saida - entrada).total_seconds() / 3600 for entrada, saida in zip(entradas, saidas)])
            return total_horas
        else:
            return None

class Departamento:
    def __init__(self, nome):
        self.nome = nome
        self.funcionarios = []

    def adicionar_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)

if __name__ == "__main__":
    departamento_ti = Departamento("TI")
    departamento_vendas = Departamento("Vendas")

    funcionario1 = Funcionario("João", "Desenvolvedor", 5000.0)
    funcionario2 = Funcionario("Maria", "Vendas", 4500.0)

    departamento_ti.adicionar_funcionario(funcionario1)
    departamento_vendas.adicionar_funcionario(funcionario2)

    funcionario1.registrar_entrada("08:00")
    funcionario1.registrar_saida("17:00")
    funcionario2.registrar_entrada("09:30")
    funcionario2.registrar_saida("18:30")

    print(f"{funcionario1.nome} trabalhou {funcionario1.calcular_horas_trabalhadas()} horas.")
    print(f"{funcionario2.nome} trabalhou {funcionario2.calcular_horas_trabalhadas()} horas.")