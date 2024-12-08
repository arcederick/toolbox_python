from flask import Flask, render_template, redirect, url_for
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'chave_secreta'

login_manager = LoginManager()
login_manager.init_app(app)

class Usuario(UserMixin):
    def __init__(self, id):
        self.id = id

@login_manager.user_loader
def carregar_usuario(id):
    return Usuario(id)

@app.route('/login')
def login():
    user = Usuario(1)
    login_user(user)
    return redirect(url_for('index'))

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return 'Deslogado com sucesso!'

@app.route('/')
@login_required
def index():
    return 'Você está logado!'

if __name__ == '__main__':
    app.run(debug=True)
