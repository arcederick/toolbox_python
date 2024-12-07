from flask import Flask, request, jsonify

app = Flask(__name__)

class Livro:
    def __init__(self, id, titulo, autor):
        self.id = id
        self.titulo = titulo
        self.autor = autor

livros = []

@app.route('/livro', methods=['POST'])
def criar_livro():
    dados = request.json
    novo_livro = Livro(len(livros) + 1, dados['titulo'], dados['autor'])
    livros.append(novo_livro)
    return jsonify({'mensagem': 'Livro criado com sucesso'})

@app.route('/livros', methods=['GET'])
def listar_livros():
    lista_livros = []
    for livro in livros:
        lista_livros.append({
            'id': livro.id,
            'titulo': livro.titulo,
            'autor': livro.autor
        })
    return jsonify({'livros': lista_livros})

if __name__ == '__main__':
    app.run(debug=True)