class Pergunta:
    def __init__(self, texto, opcoes, resposta):
        self.texto = texto
        self.opcoes = opcoes
        self.resposta = resposta

class Quiz:
    def __init__(self, perguntas):
        self.perguntas = perguntas
        self.pontuacao = 0

    def mostrar_pergunta(self):
        pergunta_atual = self.perguntas.pop(0)
        print(pergunta_atual.texto)

        for i, opcao in enumerate(pergunta_atual.opcoes, start=1):
            print(f"{i}. {opcao}")

        resposta = input("Escolha a opção correta: ")

        if resposta == pergunta_atual.resposta:
            self.pontuacao += 1
            print("Resposta correta!")
        else:
            print(f"Resposta incorreta. A resposta correta era: {pergunta_atual.resposta}")

    def iniciar_quiz(self):
        while self.perguntas:
            self.mostrar_pergunta()

        print(f"Fim do Quiz. Pontuação final: {self.pontuacao}/{len(perguntas)}")

if __name__ == "__main__":
    pergunta1 = Pergunta("Qual é a capital da França?", ["Londres", "Paris", "Madrid"], "Paris")
    pergunta2 = Pergunta("Quanto é 2 + 2?", ["3", "4", "5"], "4")
    pergunta3 = Pergunta("Qual é a cor do céu em um dia ensolarado?", ["Azul", "Verde", "Vermelho"], "Azul")

    perguntas = [pergunta1, pergunta2, pergunta3]

    quiz = Quiz(perguntas)
    quiz.iniciar_quiz()