from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def LOGIN():
    return render_template('LOGIN.html')

@app.route('/controle')
def CONTROLE():
    return render_template('CONTROLE.html')

@app.route('/movimentacao')
def MOVIMENTACAO():
    return render_template('MOVIMENTACAO.html')

@app.route('/adicionar')
def ADICIONAR():
    return render_template('ADICIONAR.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')