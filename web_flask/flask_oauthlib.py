from flask import Flask, redirect, url_for, session
from flask_oauthlib.client import OAuth

app = Flask(__name__)
app.config['SECRET_KEY'] = 'chave_secreta'
app.config['OAUTH_CREDENTIALS'] = {
    'google': {
        'id': 'seu_id',
        'secret': 'seu_segredo'
    }
}

oauth = OAuth(app)
google = oauth.remote_app(
    'google',
    consumer_key=app.config['OAUTH_CREDENTIALS']['google']['id'],
    consumer_secret=app.config['OAUTH_CREDENTIALS']['google']['secret'],
    request_token_params={'scope': 'email'},
    base_url='https://www.googleapis.com/oauth2/v1/',
    request_token_url=None,
    access_token_method='POST',
    access_token_url='https://accounts.google.com/o/oauth2/token',
    authorize_url='https://accounts.google.com/o/oauth2/auth',
)

@app.route('/')
def index():
    if 'google_token' in session:
        return f'Usuário logado com Google: {google.get("userinfo").data["email"]}'
    return redirect(url_for('login'))

@app.route('/login')
def login():
    return google.authorize(callback=url_for('authorized', _external=True))

@app.route('/logout')
def logout():
    session.pop('google_token', None)
    return redirect(url_for('index'))

@app.route('/login/authorized')
def authorized():
    resp = google.authorized_response()
    if resp is None or resp.get('access_token') is None:
        return 'Acesso negado: motivo = error_reason, erro = error_description'
    session['google_token'] = (resp['access_token'], '')
    return redirect(url_for('index'))

@google.tokengetter
def get_google_oauth_token():
    return session.get('google_token')

if __name__ == '__main__':
    app.run(debug=True)
