from datetime import datetime, timedelta

# Classe para representar uma tarefa
class Tarefa:
    def __init__(self, nome, prazo, importancia):
        self.nome = nome
        self.prazo = prazo
        self.importancia = importancia

# Lista de tarefas
tarefas = [
    Tarefa("Preparar apresentação", datetime(2023, 9, 30), 5),
    Tarefa("Responder e-mails", datetime(2023, 9, 15), 4),
    Tarefa("Reunião de equipe", datetime(2023, 9, 20), 3),
    # Adicione mais tarefas aqui
]

# Função para classificar tarefas com base na importância e no prazo
def classificar_tarefas(tarefa):
    return (-tarefa.importancia, tarefa.prazo)

# Classifica as tarefas
tarefas.sort(key=classificar_tarefas)

# Exibe as tarefas em ordem classificada
for tarefa in tarefas:
    print(f"Tarefa: {tarefa.nome}, Prazo: {tarefa.prazo}, Importância: {tarefa.importancia}")