from flask import Flask, render_template

app = Flask(__name__,
            static_url_path='',
            static_folder='app/static',
            template_folder='app/templates')

@app.route('/hello-to-training')
def index():
    return render_template('public/index.html')
    