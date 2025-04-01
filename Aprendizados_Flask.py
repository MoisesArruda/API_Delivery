from flask import Flask, Response, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import json

# Criando uma instancia do Flask
app = Flask(__name__)

# # Criando uma rota para a página inicial
# @app.route('/')
# # O que a API vai responder
# def hello_world():
#     return "Hello, World!"

# # Quando desenvolvemos uma API, é importante que ela esteja em modo de Debug para que possamos ver os erros
# app.config['DEBUG'] = True
# app.run()

# Conexão com o banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = \
    '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
        SGBD = 'mysql+mysqlconnector',
        usuario = 'root',
        senha = 'admin',
        servidor = 'localhost',
        database = 'delivery'
    )

db = SQLAlchemy(app)
ma = Marshmallow(app)

class Pedido(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cliente = db.Column(db.String(100), nullable=False)
    produto = db.Column(db.String(100), nullable=False)
    valor = db.Column(db.Float, nullable=False)

# ORM - Serialização e Deserialização de dados
class PedidoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Pedido
        load_instance = True
        sqla_session = db.session

# Endpoint da API, URL que vamos acessar para fazer uma requisição(Operação CRUD)
@app.route('/')
def lista_pedidos():
    # Retorna todos os pedidos
    pedidos = Pedido.query.all()
    # Serialização de dados
    pedido_schema = PedidoSchema(many=True)
    # Retorna os dados serializados
    return pedido_schema.dump(pedidos)

# Endpoint para criar um novo pedido, 'Post' é método HTTP para criar recurso
@app.route('/criapedido', methods=['POST'])
def cria_pedido():
    cliente = request.json['cliente']
    produto = request.json['produto']
    valor = request.json['valor']

    novo_pedido = Pedido(cliente=cliente, produto=produto, valor=valor)
    # Adiciona o novo pedido ao banco de dados
    db.session.add(novo_pedido)
    # Salva as alterações no banco de dados
    db.session.commit() 

    pedido_schema = PedidoSchema()
    return pedido_schema.dump(novo_pedido)

# Endpoint para ler um pedido
@app.route('/pedido/<int:id>', methods=['GET'])
def le_pedido(id):
    # Retorna o pedido com o id informado
    pedido = Pedido.query.filter(Pedido.id == id).one_or_none()
    if pedido is not None:
        pedido_schema = PedidoSchema()
        return pedido_schema.dump(pedido)
    else:
        return {'message': 'Pedido não encontrado'}, 404

# Endpoint para atualizar um pedido
@app.route('/pedido/<int:id>', methods=['PUT'])
def atualiza_pedido(id):
    pedido = Pedido.query.filter(Pedido.id == id).one_or_none()
    if pedido is not None:
        pedido.cliente = request.json['cliente']
        pedido.produto = request.json['produto']
        pedido.valor = request.json['valor']

        # Salva as alterações no banco de dados
        db.session.merge(pedido)
        db.session.commit()
        pedido_schema = PedidoSchema()
        return pedido_schema.dump(pedido)
    else:
        return {'message': 'Pedido não encontrado'}, 404

# Endpoint para deletar um pedido
@app.route('/pedido/<int:id>', methods=['DELETE'])
def apaga_pedido(id):
    pedido = Pedido.query.filter(Pedido.id == id).one_or_none()
    if pedido is not None:
        db.session.delete(pedido)
        db.session.commit()
        pedido_schema = PedidoSchema()
        return pedido_schema.dump(pedido)
    else:
        return {'message': 'Pedido não encontrado'}, 404

if __name__ == '__main__':
    app.config['DEBUG'] = True
    app.run()

# {
#     "cliente": "João da Silva",
#     "produto": "Pizza",
#     "valor": 30.0
# }

# {
#     "cliente": "Maria Eduarda",
#     "produto": "Milkshake",
#     "valor": 15.0
# }