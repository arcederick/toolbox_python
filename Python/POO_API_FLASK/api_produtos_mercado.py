from flask import Flask, request, jsonify

app = Flask(__name__)

class Produto:
    def __init__(self, id, nome, preco):
        self.id = id
        self.nome = nome
        self.preco = preco

produtos = []

@app.route('/produto', methods=['POST'])
def criar_produto():
    dados = request.json
    novo_produto = Produto(len(produtos) + 1, dados['nome'], dados['preco'])
    produtos.append(novo_produto)
    return jsonify({'mensagem': 'Produto criado com sucesso'})

@app.route('/produtos', methods=['GET'])
def listar_produtos():
    lista_produtos = []
    for produto in produtos:
        lista_produtos.append({
            'id': produto.id,
            'nome': produto.nome,
            'preco': produto.preco
        })
    return jsonify({'produtos': lista_produtos})

if __name__ == '__main__':
    app.run(debug=True)