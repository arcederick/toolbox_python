from flask import Flask, request, jsonify

app = Flask(__name__)

class Cliente:
    def __init__(self, id, nome, email):
        self.id = id
        self.nome = nome
        self.email = email

clientes = []

@app.route('/cliente', methods=['POST'])
def criar_cliente():
    dados = request.json
    novo_cliente = Cliente(len(clientes) + 1, dados['nome'], dados['email'])
    clientes.append(novo_cliente)
    return jsonify({'mensagem': 'Cliente criado com sucesso'})

@app.route('/clientes', methods=['GET'])
def listar_clientes():
    lista_clientes = []
    for cliente in clientes:
        lista_clientes.append({
            'id': cliente.id,
            'nome': cliente.nome,
            'email': cliente.email
        })
    return jsonify({'clientes': lista_clientes})

if __name__ == '__main__':
    app.run(debug=True)