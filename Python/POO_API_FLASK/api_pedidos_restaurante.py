from flask import Flask, request, jsonify

app = Flask(__name__)

class Pedido:
    def __init__(self, id, prato, quantidade):
        self.id = id
        self.prato = prato
        self.quantidade = quantidade

pedidos = []

@app.route('/pedido', methods=['POST'])
def criar_pedido():
    dados = request.json
    novo_pedido = Pedido(len(pedidos) + 1, dados['prato'], dados['quantidade'])
    pedidos.append(novo_pedido)
    return jsonify({'mensagem': 'Pedido criado com sucesso'})

@app.route('/pedidos', methods=['GET'])
def listar_pedidos():
    lista_pedidos = []
    for pedido in pedidos:
        lista_pedidos.append({
            'id': pedido.id,
            'prato': pedido.prato,
            'quantidade': pedido.quantidade
        })
    return jsonify({'pedidos': lista_pedidos})

if __name__ == '__main__':
    app.run(debug=True)