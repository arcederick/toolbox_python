from flask import Flask, request, jsonify

app = Flask(__name__)

class ClienteVIP:
    def __init__(self, id, nome, nivel):
        self.id = id
        self.nome = nome
        self.nivel = nivel

clientes_vip = []

@app.route('/cliente_vip', methods=['POST'])
def criar_cliente_vip():
    dados = request.json
    novo_cliente_vip = ClienteVIP(len(clientes_vip) + 1, dados['nome'], dados['nivel'])
    clientes_vip.append(novo_cliente_vip)
    return jsonify({'mensagem': 'Cliente VIP criado com sucesso'})

@app.route('/clientes_vip', methods=['GET'])
def listar_clientes_vip():
    lista_clientes_vip = []
    for cliente_vip in clientes_vip:
        lista_clientes_vip.append({
            'id': cliente_vip.id,
            'nome': cliente_vip.nome,
            'nivel': cliente_vip.nivel
        })
    return jsonify({'clientes_vip': lista_clientes_vip})

if __name__ == '__main__':
    app.run(debug=True)