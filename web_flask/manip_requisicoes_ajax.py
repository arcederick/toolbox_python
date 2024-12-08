from flask import Flask, jsonify, request
from flask_jwt import JWT, jwt_required, current_identity

app = Flask(__name__)
app.config['SECRET_KEY'] = 'chave_secreta'

users = {
    'usuario': 'senha'
}

def autenticar(username, password):
    if username in users and users[username] == password:
        return username

def identidade(payload):
    user_id = payload['identity']
    return {'user_id': user_id}

jwt = JWT(app, autenticar, identidade)

@app.route('/protegido')
@jwt_required()
def protegido():
    return jsonify(user_id=current_identity['user_id'])

if __name__ == '__main__':
    app.run(debug=True)
