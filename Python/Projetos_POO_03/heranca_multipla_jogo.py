class HabilidadeFisica:
    def __init__(self, nome, dano):
        self.nome = nome
        self.dano = dano

    def usar(self):
        return f"{self.nome} causou {self.dano} pontos de dano físico."

class HabilidadeMágica:
    def __init__(self, nome, poder):
        self.nome = nome
        self.poder = poder

    def usar(self):
        return f"{self.nome} usou poder mágico com força {self.poder}."

class Jogador(HabilidadeFisica, HabilidadeMágica):
    def __init__(self, nome, dano, poder):
        HabilidadeFisica.__init__(self, nome, dano)
        HabilidadeMágica.__init__(self, nome, poder)

class Monstro(HabilidadeFisica):
    def __init__(self, nome, dano):
        HabilidadeFisica.__init__(self, nome, dano)

if __name__ == "__main__":
    jogador1 = Jogador("Guerreiro", 30, 10)
    monstro1 = Monstro("Dragão", 50)

    print(jogador1.usar())
    print(monstro1.usar())