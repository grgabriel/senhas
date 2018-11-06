from flask import Flask, render_template
#from win_funcs import imprimir
from lin_funcs import imprimir

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/senhas/<num>')
def numero(num):
    if not int(num) == 0:
        imprimir(num)

    if num == 99:
        prox = 0
    else:
        prox = int(num) + 1

    dict = {'prox':prox, 'num':num}
    return render_template('senhas.html', numeros = dict)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
