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


@app.route('/controle', methods=["POST", "GET"])
def CONTROLE():

    conexao = obter_conexao()
    cursor = conexao.cursor()

    if request.method == 'GET':
        cursor.execute("SELECT * FROM estoque")

        produtos = cursor.fetchall()

        return render_template(
            "CONTROLE.html",
            resultado=produtos
        )
    else:

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

@app.route('/estoque', methods=['POST', 'GET'])
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

    # Puxa os dados para popular o <select> do formulário
    cursor.execute("""
        SELECT id, nome, quantidade_disponivel
        FROM estoque
    """)
    produtos = cursor.fetchall()

    # Puxa todo o histórico salvo na tabela 'historico' (ordenado pelo ID mais recente)
    cursor.execute("""
        SELECT id, nome_produto, tipo, quantidade, usuario, DATE_FORMAT(data_registro, '%d/%m/%Y %H:%i') 
        FROM historico 
        ORDER BY id DESC
    """)
    historico = cursor.fetchall()

    cursor.close()
    conexao.close()

    return render_template(
        "MOVIMENTACAO.html",
        produtos=produtos,
        historico=historico
    )


@app.route('/salvar_movimentacao', methods=['POST'])
def SALVAR_MOVIMENTACAO():
    id_produto = request.form.get('produto')
    tipo_movimentacao = request.form.get('tipo')  # "Entrada" ou "Saida"
    quantidade_movida = int(request.form.get('quantidade'))
    
    # Usuário temporário (como a sessão de login ainda não está ativa globalmente)
    usuario_atual = "Almoxarife" 

    conexao = obter_conexao()
    cursor = conexao.cursor()

    try:
        # 1. Recupera o nome e a quantidade atual do produto selecionado
        cursor.execute("SELECT nome, quantidade_disponivel FROM estoque WHERE id = %s", (id_produto,))
        produto = cursor.fetchone()
        
        if produto is None:
            return "Produto não encontrado!", 404
            
        nome_produto = produto[0]
        quantidade_atual = produto[1]

        # 2. Calcula a alteração do estoque
        if tipo_movimentacao == "Entrada":
            nova_quantidade = quantidade_atual + quantidade_movida
        else:  # Saída
            if quantidade_movida > quantidade_atual:
                return f"Erro: Estoque insuficiente! Quantidade disponível: {quantidade_atual}", 400
            nova_quantidade = quantidade_atual - quantidade_movida

        # 3. Atualiza a tabela estoque
        cursor.execute(
            "UPDATE estoque SET quantidade_disponivel = %s WHERE id = %s",
            (nova_quantidade, id_produto)
        )

        # 4. Grava no Histórico de Movimentações usando NOW() para carregar a data/hora atual
        cursor.execute("""
            INSERT INTO historico (nome_produto, tipo, quantidade, usuario, data_registro) 
            VALUES (%s, %s, %s, %s, NOW())
        """, (nome_produto, tipo_movimentacao, quantidade_movida, usuario_atual))

        # Confirma as alterações transacionais no MySQL
        conexao.commit()

    except Exception as e:
        conexao.rollback()
        return f"Erro na base de dados: {str(e)}", 500
    finally:
        cursor.close()
        conexao.close()

    # Redireciona de volta para recarregar as tabelas atualizadas na tela de movimentação
    return redirect('/movimentacao')


# ---------------- EXECUTAR ---------------- #

if __name__ == "__main__":
    app.run(debug=True)