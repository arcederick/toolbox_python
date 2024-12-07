from flask import Flask, request, jsonify

app = Flask(__name__)

class Funcionario:
    def __init__(self, id, nome, cargo):
        self.id = id
        self.nome = nome
        self.cargo = cargo

funcionarios = []

@app.route('/funcionario', methods=['POST'])
def criar_funcionario():
    dados = request.json
    novo_funcionario = Funcionario(len(funcionarios) + 1, dados['nome'], dados['cargo'])
    funcionarios.append(novo_funcionario)
    return jsonify({'mensagem': 'Funcionário criado com sucesso'})

@app.route('/funcionarios', methods=['GET'])
def listar_funcionarios():
    lista_funcionarios = []
    for funcionario in funcionarios:
        lista_funcionarios.append({
            'id': funcionario.id,
            'nome': funcionario.nome,
            'cargo': funcionario.cargo
        })
    return jsonify({'funcionarios': lista_funcionarios})

if __name__ == '__main__':
    app.run(debug=True)