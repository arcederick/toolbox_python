from flask import Flask, render_template, request
from flask_mail import Mail, Message

app = Flask(__name__)
app.config['SECRET_KEY'] = 'chave_secreta'
app.config['MAIL_SERVER'] = 'smtp.example.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'seu_email@example.com'
app.config['MAIL_PASSWORD'] = 'sua_senha'
app.config['MAIL_USE_TLS'] = True

mail = Mail(app)

@app.route('/enviar-email', methods=['GET', 'POST'])
def enviar_email():
    if request.method == 'POST':
        destinatario = request.form['destinatario']
        assunto = request.form['assunto']
        corpo = request.form['corpo']
        msg = Message(assunto, sender='seu_email@example.com', recipients=[destinatario])
        msg.body = corpo
        mail.send(msg)
        return 'Email enviado com sucesso!'
    return render_template('formulario_email.html')

if __name__ == '__main__':
    app.run(debug=True)
