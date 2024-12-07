from flask import Flask, request, jsonify

app = Flask(__name__)

class Tarefa:
    def __init__(self, id, descricao, concluida):
        self.id = id
        self.descricao = descricao
        self.concluida = concluida

tarefas = []

@app.route('/tarefa', methods=['POST'])
def criar_tarefa():
    dados = request.json
    nova_tarefa = Tarefa(len(tarefas) + 1, dados['descricao'], False)
    tarefas.append(nova_tarefa)
    return jsonify({'mensagem': 'Tarefa criada com sucesso'})

@app.route('/tarefas', methods=['GET'])
def listar_tarefas():
    lista_tarefas = []
    for tarefa in tarefas:
        lista_tarefas.append({
            'id': tarefa.id,
            'descricao': tarefa.descricao,
            'concluida': tarefa.concluida
        })
    return jsonify({'tarefas': lista_tarefas})

if __name__ == '__main__':
    app.run(debug=True)