from flask import Flask, request
from flask_uploads import UploadSet, configure_uploads

app = Flask(__name__)
uploads = UploadSet('uploads', extensions=('txt', 'pdf', 'docx'))
app.config['UPLOADED_UPLOADS_DEST'] = 'uploads'
configure_uploads(app, uploads)

@app.route('/upload', methods=['POST'])
def upload_arquivo():
    arquivo = request.files['arquivo']
    if arquivo:
        filename = uploads.save(arquivo)
        return f'Arquivo {filename} enviado com sucesso!'
    return 'Nenhum arquivo enviado.'

if __name__ == '__main__':
    app.run(debug=True)
