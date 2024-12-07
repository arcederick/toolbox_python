import random

class Transacao:
    def __init__(self, id, valor, descricao):
        self.id = id
        self.valor = valor
        self.descricao = descricao

class DetectorFraude:
    def __init__(self):
        self.transacoes = []

    def adicionar_transacao(self, transacao):
        self.transacoes.append(transacao)

    def detectar_fraude(self):
        # Implemente a lógica de detecção de fraude aqui (por exemplo, com base em valores ou descrições suspeitas)
        return random.choice([True, False])

if __name__ == "__main__":
    detector = DetectorFraude()

    transacao1 = Transacao(1, 100.0, "Compra online em loja desconhecida")
    transacao2 = Transacao(2, 50.0, "Restaurante local")
    transacao3 = Transacao(3, 200.0, "Compra online em loja confiável")

    detector.adicionar_transacao(transacao1)
    detector.adicionar_transacao(transacao2)
    detector.adicionar_transacao(transacao3)

    if detector.detectar_fraude():
        print("Fraude detectada!")
    else:
        print("Nenhuma fraude detectada.")