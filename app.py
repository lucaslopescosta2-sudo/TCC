from flask import Flask, render_template, request
import mysql.connector
import bcrypt

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

@app.route('/login_invalido')
def LOGIN_invalido():
    return render_template('LOGIN_invalido.html')

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
        return render_template('LOGIN_invalido.html')
    
    if resultado is not None:

        login_valido = bcrypt.checkpw(senha_digitada.encode('utf-8'), resultado[1].encode('utf-8'))
        
        if login_valido:
            conexao = obter_conexao()
            cursor = conexao.cursor()
            cursor.execute("select * from estoque")

            resultado = cursor.fetchall()
        
        else:
            return render_template('LOGIN_invalido.html')
        
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