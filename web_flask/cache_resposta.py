from flask import Flask
from flask_caching import Cache

app = Flask(__name__)
app.config['SECRET_KEY'] = 'chave_secreta'
app.config['CACHE_TYPE'] = 'simple'

cache = Cache(app)

@app.route('/resultado')
@cache.cached(timeout=300)
def resultado():
    # Lógica para gerar o resultado
    return 'Resultado da operação'

if __name__ == '__main__':
    app.run(debug=True)
