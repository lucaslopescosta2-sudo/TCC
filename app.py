from flask import Flask, render_template, request, redirect
import mysql.connector
import bcrypt

app = Flask(__name__)


def obter_conexao():

    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="db_almox",
        port=3306
    )


# ---------------- LOGIN ---------------- #

@app.route('/')
def LOGIN():
    return render_template("LOGIN.html")


@app.route('/login_invalido')
def LOGIN_INVALIDO():
    return render_template("LOGIN_invalido.html")


@app.route('/controle', methods=["POST"])
def CONTROLE():

    conexao = obter_conexao()
    cursor = conexao.cursor()

    usuario = request.form.get("usuario")
    senha = request.form.get("senha")

    cursor.execute(
        "SELECT usuario, senha FROM usuarios WHERE usuario=%s",
        (usuario,)
    )

    resultado = cursor.fetchone()

    if resultado is None:
        return render_template("LOGIN_invalido.html")

    senha_correta = bcrypt.checkpw(
        senha.encode("utf-8"),
        resultado[1].encode("utf-8")
    )

    if not senha_correta:
        return render_template("LOGIN_invalido.html")

    cursor.execute("SELECT * FROM estoque")

    produtos = cursor.fetchall()

    return render_template(
        "CONTROLE.html",
        resultado=produtos
    )


# ---------------- ESTOQUE ---------------- #

@app.route('/estoque')
def ESTOQUE():

    conexao = obter_conexao()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM estoque")

    produtos = cursor.fetchall()

    return render_template(
        "CONTROLE.html",
        resultado=produtos
    )


# ---------------- MOVIMENTAÇÃO ---------------- #

@app.route('/movimentacao')
def MOVIMENTACAO():

    conexao = obter_conexao()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT id, nome, quantidade_disponivel
        FROM estoque
    """)
    produtos = cursor.fetchall()

    cursor.execute("""
        SELECT m.id,
               e.nome,
               m.tipo,
               m.quantidade,
               m.usuario,
               m.data_movimentacao
        FROM movimentacao m
        INNER JOIN estoque e
        ON m.produto_id = e.id
        ORDER BY m.data_movimentacao DESC
    """)
    historico = cursor.fetchall()

    return render_template(
        "MOVIMENTACAO.html",
        produtos=produtos,
        historico=historico
    )
# ---------------- ADICIONAR ---------------- #

@app.route('/adicionar')
def ADICIONAR():

    return render_template("ADICIONAR.html")


# ---------------- EXECUTAR ---------------- #

if __name__ == "__main__":
    app.run(debug=True)