from flask import Flask, render_template_string
from flask_flatpages import FlatPages

app = Flask(__name__)
app.config['FLATPAGES_AUTO_RELOAD'] = True
app.config['FLATPAGES_EXTENSION'] = '.md'
pages = FlatPages(app)

@app.route('/')
def index():
    return render_template_string(pages.get('index').html)

if __name__ == '__main__':
    app.run(debug=True)
