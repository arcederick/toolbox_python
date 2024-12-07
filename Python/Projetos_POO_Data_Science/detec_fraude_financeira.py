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
        total_transacoes = len(self.transacoes)
        if total_transacoes < 3:
            return "Não há transações suficientes para detecção de fraude."
        
        ultima_transacao = self.transacoes[-1]
        penultima_transacao = self.transacoes[-2]
        antepenultima_transacao = self.transacoes[-3]

        if (
            ultima_transacao.valor > 1000 and
            penultima_transacao.valor > 1000 and
            antepenultima_transacao.valor > 1000
        ):
            return "Possível fraude detectada: Três transações de alto valor consecutivas."

        return "Nenhuma atividade de fraude detectada."

if __name__ == "__main__":
    # Crie um detector de fraude e adicione algumas transações
    detector_fraude = DetectorFraude()
    transacao1 = Transacao(1, 500, "Compra Online")
    transacao2 = Transacao(2, 1200, "Retirada em Caixa Eletrônico")
    transacao3 = Transacao(3, 1100, "Compra em Loja")
    detector_fraude.adicionar_transacao(transacao1)
    detector_fraude.adicionar_transacao(transacao2)
    detector_fraude.adicionar_transacao(transacao3)

    # Detectar fraude
    resultado = detector_fraude.detectar_fraude()
    print(resultado)