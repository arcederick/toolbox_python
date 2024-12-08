from flask import Flask, session, redirect, url_for

app = Flask(__name__)
app.config['SECRET_KEY'] = 'chave_secreta'
app.config['SESSION_TYPE'] = 'filesystem'

@app.route('/login/<username>')
def login(username):
    session['username'] = username
    return redirect(url_for('index'))

@app.route('/')
def index():
    if 'username' in session:
        return f'Bem-vindo, {session["username"]}!'
    return 'Você não está logado!'

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
