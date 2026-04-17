from flask import Flask, render_template

app = Flask(__name__)

#exercício 2
@app.route('/ping')
def pagina_ping():
    return "<h1>Pong!"

#exercício 3
@app.route('/')
def pagina_inicial():
    return "<h1>Bruna Monique</h1>" \
    "<h3>Turma de Desenvolvimento de Sistemas do Senai.</h3>"\
    "<h3> Tema escolhido: Streaming!</h3>"

#exercício 4
@app.route('/login')
def exibe_login():
    return "<h1>Página de login.</h1>"

@app.route('/cadastro')
def exibe_cadastro():
    return "<h1>Página de cadastro.</h1>"

@app.route('/sobre')
def exibe_sobre():
    return "<h1>Você está em site de streaming .</h1>"

#exercício 6
@app.route('/teste')
def apresentar_site():
    return render_template('teste.html')

#exercício 7
@app.route('/erro')
def provocar_erro():
    resultado = 10 / 0
    return f"Oresultado é {resultado}"

#exercício 9
@app.errorhandler(404)
def pagina_nao_encontrada(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(port=8080, debug=True)