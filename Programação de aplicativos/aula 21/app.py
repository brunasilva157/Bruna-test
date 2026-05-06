from flask import Flask, request, redirect, url_for, render_template, flash

app = Flask(__name__)
app.secret_key = "minha_chave_secreta"

# --- MODELO ---
class Filme:
    def __init__(self, titulo, genero, tempo):
        self.titulo = titulo
        self.genero = genero
        self.tempo = tempo

class FilmeDAO:
    def __init__(self):
        self.banco_de_dados = []
    def salvar(self, filme):
        self.banco_de_dados.append(filme)
    def listar(self):
        return self.banco_de_dados

dao = FilmeDAO()

# --- ROTAS ---

@app.route('/')
def index():
    # Carrega a página do formulário
    return render_template('formulario.html')

@app.route('/lista')
def mostrar_lista():
    filmes_guardados = dao.listar()
    # O HTML espera a variável "filmes"
    return render_template('lista.html', filmes=filmes_guardados)

@app.route('/salvar_filme', methods=['POST'])
def salvar_filme():
    titulo = request.form.get("titulo")
    genero = request.form.get("genero")
    tempo_input = request.form.get("tempo")

    if not titulo or not genero or not tempo_input:
        flash("Erro: Todos os campos devem ser preenchidos!")
        return redirect(url_for('index'))

    try:
        novo = Filme(titulo, genero, tempo_input)
        dao.salvar(novo)
        
        flash("Filme cadastrado com sucesso!")
        return redirect(url_for('mostrar_lista'))

    except Exception as e:
        flash(f"Erro ao salvar: {e}")
        return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)