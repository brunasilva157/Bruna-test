import sqlite3
conexao = sqlite3.connect("meu_sistema.db")
cursor = conexao.cursor()

#1. Busca todos os registros
cursor.execute("SELECT id, nome, preco FROM produtos") # Ajustado o nome do campo id
resultado_bruto = cursor.fetchall()

#2. Processo de Transformação
lista_produtos_tratada = []
for linha in resultado_bruto:
    produto_dicionario = {
        "id": linha[0],
        "nome": linha[1],
        "preco_unitario": linha[2]
    }
    lista_produtos_tratada.append(produto_dicionario)

conexao.close()

#3. Consumo dos dados
print("--- RELATÓRIO DO SISTEMA ---")
for produto in lista_produtos_tratada:
    print(f"[{produto['id']}] Item: {produto['nome']} | Valor: R$ {produto['preco_unitario']:.2f}")