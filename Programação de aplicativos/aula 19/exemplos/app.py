from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def pagina_inicial():
    return "<h1>Olá, Mundo! Este é o back-end respondendo.</h1>"

@app.route('/meusite')
def apresentar_site():
    return render_template('index.html')

@app.route('/aula18')
def apresentar_aula18():
    return render_template('aula18.html')

@app.route('/contato')
def exibe_contato():
    return "<h1>Meu email de contato é bruna@gmail.com.</h1>"

if __name__ == '__main__':
    app.run(debug=True)