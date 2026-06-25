from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def LOGIN():
    return render_template('LOGIN.html')

@app.route('/CONTROLE.html')
def CONTROLE():
    return render_template('CONTROLE.html')

@app.route('/MOVIMENTACAO.html')
def MOVIMENTACAO():
    return render_template('MOVIMENTACAO.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
