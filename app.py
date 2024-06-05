from flask import Flask, render_template
from lin_funcs import imprimir

app = Flask(__name__)

# Main index, serve a basic page to set number to 0
@app.route('/')
def index():
    return render_template('index.html')

# Serve the "your ticket" page, ready to print number 'num'
@app.route('/senhas/<num>')
def numero(num):    
    if int(num) == 99:
        prox = 1
    else:
        prox = int(num) + 1
    if int(num) == 100:
        num = 0

    dict = {'prox':prox, 'num':num}
    return render_template('senhas.html', numeros = dict)

# Print number 'num' then open "your ticket" page with next number
@app.route('/senhas/print/<num>')
def imprime(num):
    if not int(num) == 0:
        imprimir(num)
    
    if int(num) == 99:
        prox = 1
    else:
        prox = int(num) + 1
    if int(num) == 100:
        num = 0
    dict = {'prox':prox, 'num':num}
    return render_template('imprimir.html', numeros = dict)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
