from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)


def obter_conexao():
      
      return mysql.connector.connect(
         host='localhost',
         port= 3306,
         password = 'root',
         database = 'db_almox',
         user = 'root'
      )

@app.route('/')
def LOGIN():
        
    return render_template('LOGIN.html')

@app.route('/controle', methods=['POST', 'GET'])
def CONTROLE():

    conexao = obter_conexao()
    cursor = conexao.cursor()
        
    usuario_digitado = request.form.get('usuario')
    senha_digitada = request.form.get('senha')
    valores = (usuario_digitado,)
    cursor.execute("SELECT usuario, senha FROM usuarios WHERE usuario = %s", valores)

    resultado = cursor.fetchone()

    print(usuario_digitado)

    if resultado is None:
        return "Usuario inexistente"
    
    if resultado is not None:
        if senha_digitada == resultado[1]:
            conexao = obter_conexao()
            cursor = conexao.cursor()
            cursor.execute("select * from estoque")

            resultado = cursor.fetchall()

    conexao = mysql.connector.connect(
        host = 'localhost',
        password = 'root',
        user = 'root',
        database = 'db_almox'
)

    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM estoque")

    resultado = cursor
        
    return render_template('CONTROLE.html', resultado=resultado)


@app.route('/movimentacao')
def MOVIMENTACAO():

    conexao = obter_conexao()

    cursor = conexao.cursor()
    cursor.execute("select * from estoqu")

    resultado = cursor.fetchall()

    return render_template('MOVIMENTACAO.html')

@app.route('/adicionar')
def ADICIONAR():





    return render_template('ADICIONAR.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')