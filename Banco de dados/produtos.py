#DESAFIO: Corrija o script abaixo
import sqlite3

def criar_tabela_produto():
    conexao = sqlite3.connect("sistema_de_produtos.db")
    cursor = conexao.cursor()

    nome_produto = "macarrão"
    preco_produto = 15.00

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS produto (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        preco REAL NOT NULL
    )
    """)

    comando_sql = "INSERT INTO produto (nome, preco) VALUES (?, ?)"
    valores = (nome_produto, preco_produto)
    cursor.execute(comando_sql, valores)

    conexao.commit()
    cursor.close()
    conexao.close()

print("Produto cadastrado!")