from datetime import datetime

class Evento:
    def __init__(self, titulo, data, hora, local):
        self.titulo = titulo
        self.data = data
        self.hora = hora
        self.local = local

    def __str__(self):
        return (
            f"Título: {self.titulo}\n"
            f"Data: {self.data}\n"
            f"Hora: {self.hora}\n"
            f"Local: {self.local}\n"
        )

class AgendaEventos:
    def __init__(self):
        self.eventos = []

    def adicionar_evento(self, evento):
        self.eventos.append(evento)

    def editar_evento(self, indice, novo_evento):
        if 0 <= indice < len(self.eventos):
            self.eventos[indice] = novo_evento

    def remover_evento(self, indice):
        if 0 <= indice < len(self.eventos):
            del self.eventos[indice]

    def listar_eventos(self):
        return self.eventos

if __name__ == "__main__":
    agenda = AgendaEventos()

    # Adicionar eventos
    evento1 = Evento("Conferência de Tecnologia", "2023-12-10", "15:00", "Centro de Convenções")
    evento2 = Evento("Reunião de Equipe", "2023-11-20", "10:30", "Escritório Principal")

    agenda.adicionar_evento(evento1)
    agenda.adicionar_evento(evento2)

    # Listar eventos
    eventos = agenda.listar_eventos()
    for i, evento in enumerate(eventos):
        print(f"Evento {i + 1}:\n{evento}")

    # Editar evento
    novo_evento = Evento("Reunião de Equipe (Atualizada)", "2023-11-20", "11:00", "Escritório Principal")
    agenda.editar_evento(1, novo_evento)

    # Listar eventos atualizados
    print("\nLista de Eventos Atualizada:")
    eventos = agenda.listar_eventos()
    for i, evento in enumerate(eventos):
        print(f"Evento {i + 1}:\n{evento}")

    # Remover evento
    agenda.remover_evento(0)

    # Listar eventos após a remoção
    print("\nLista de Eventos Após Remoção:")
    eventos = agenda.listar_eventos()
    for i, evento in enumerate(eventos):
        print(f"Evento {i + 1}:\n{evento}")