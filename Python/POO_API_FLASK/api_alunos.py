from flask import Flask, request, jsonify

app = Flask(__name__)

class Aluno:
    def __init__(self, id, nome, curso):
        self.id = id
        self.nome = nome
        self.curso = curso

alunos = []

@app.route('/aluno', methods=['POST'])
def criar_aluno():
    dados = request.json
    novo_aluno = Aluno(len(alunos) + 1, dados['nome'], dados['curso'])
    alunos.append(novo_aluno)
    return jsonify({'mensagem': 'Aluno criado com sucesso'})

@app.route('/alunos', methods=['GET'])
def listar_alunos():
    lista_alunos = []
    for aluno in alunos:
        lista_alunos.append({
            'id': aluno.id,
            'nome': aluno.nome,
            'curso': aluno.curso
        })
    return jsonify({'alunos': lista_alunos})

if __name__ == '__main__':
    app.run(debug=True)