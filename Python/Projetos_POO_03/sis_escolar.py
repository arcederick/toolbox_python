class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def info(self):
        return f"Nome: {self.nome}, Idade: {self.idade}"

class Aluno(Pessoa):
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade)
        self.matricula = matricula

    def info(self):
        return f"Aluno - {super().info()}, Matrícula: {self.matricula}"

class Professor(Pessoa):
    def __init__(self, nome, idade, disciplina):
        super().__init__(nome, idade)
        self.disciplina = disciplina

    def info(self):
        return f"Professor - {super().info()}, Disciplina: {self.disciplina}"

class FuncionarioAdministrativo(Pessoa):
    def __init__(self, nome, idade, cargo):
        super().__init__(nome, idade)
        self.cargo = cargo

    def info(self):
        return f"Funcionário Administrativo - {super().info()}, Cargo: {self.cargo}"

if __name__ == "__main__":
    aluno1 = Aluno("João", 18, "A12345")
    professor1 = Professor("Maria", 35, "Matemática")
    admin1 = FuncionarioAdministrativo("Carlos", 40, "Secretário")

    print(aluno1.info())
    print(professor1.info())
    print(admin1.info())