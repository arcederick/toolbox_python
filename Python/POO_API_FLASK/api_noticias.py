from flask import Flask, request, jsonify

app = Flask(__name__)

class Noticia:
    def __init__(self, id, titulo, conteudo):
        self.id = id
        self.titulo = titulo
        self.conteudo = conteudo

noticias = []

@app.route('/noticia', methods=['POST'])
def criar_noticia():
    dados = request.json
    nova_noticia = Noticia(len(noticias) + 1, dados['titulo'], dados['conteudo'])
    noticias.append(nova_noticia)
    return jsonify({'mensagem': 'Notícia criada com sucesso'})

@app.route('/noticias', methods=['GET'])
def listar_noticias():
    lista_noticias = []
    for noticia in noticias:
        lista_noticias.append({
            'id': noticia.id,
            'titulo': noticia.titulo,
            'conteudo': noticia.conteudo
        })
    return jsonify({'noticias': lista_noticias})

if __name__ == '__main__':
    app.run(debug=True)