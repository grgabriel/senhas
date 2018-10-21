from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/senhas')
def index():
    return render_template('senha.html', num=1)

@app.route('/senhas/<num>')
def numer(num):
    return render_template('senha.html', num=num)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
