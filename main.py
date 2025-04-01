from flask import Flask, Response

# Criando uma instancia do Flask
app = Flask(__name__)

# Criando uma rota para a página inicial
@app.route('/')
# O que a API vai responder
def hello_world():
    return "Hello, World!"

# Quando desenvolvemos uma API, é importante que ela esteja em modo de Debug para que possamos ver os erros
app.config['DEBUG'] = True
app.run()
