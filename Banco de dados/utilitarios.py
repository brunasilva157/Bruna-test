import sqlite3

# #1. Estabelecendo a conexão
conexao = sqlite3.connect("sistema_de_matricula.db")
cursor = conexao.cursor()

# #2. Dados hipotéticos
nome_aluno = "Bruna"
matricula_aluno = 25485182148

# #3. Garante que a tabela exista (Ajustada para Alunos)
cursor.execute("""
CREATE TABLE IF NOT EXISTS alunos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    matricula INTEGER NOT NULL
)
""")

# #4. Execução da query (Ajustada para a tabela 'alunos')
comando_sql = "INSERT INTO alunos (nome, matricula) VALUES (?, ?)"
valores = (nome_aluno, matricula_aluno)
cursor.execute(comando_sql, valores)

# #5. Confirmação e Encerramento
conexao.commit()
cursor.close()
conexao.close()

print("Matrícula feita com sucesso!")