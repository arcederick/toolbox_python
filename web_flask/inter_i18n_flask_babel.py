from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
app.config['SECRET_KEY'] = 'chave_secreta'
app.config['BABEL_DEFAULT_LOCALE'] = 'pt'

babel = Babel(app)

@babel.localeselector
def get_locale():
    # Lógica para selecionar o idioma do usuário
    return 'pt'  # Exemplo: retornar 'pt' para português

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
