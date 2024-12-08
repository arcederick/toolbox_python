from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'chave_secreta'

class MeuFormulario(FlaskForm):
    nome = StringField('Nome')
    enviar = SubmitField('Enviar')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = MeuFormulario()
    if form.validate_on_submit():
        nome = form.nome.data
        return f'Olá, {nome}!'
    return render_template('formulario.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
