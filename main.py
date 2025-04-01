from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

# Carrega as variáveis de ambiente
load_dotenv()

# Inicializa a aplicação Flask
app = Flask(__name__)

# Configuração do banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///delivery.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializa o SQLAlchemy
db = SQLAlchemy(app)

# Inicializa o Flask-Migrate
migrate = Migrate(app, db)

# Rota principal
@app.route('/')
def index():
    return jsonify({
        'message': 'Bem-vindo à API de Delivery',
        'status': 'online'
    })

# Modelos
class Cliente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    telefone = db.Column(db.String(20))
    endereco = db.Column(db.String(200))
    pedidos = db.relationship('Pedido', backref='cliente', lazy=True)

class Entregador(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    telefone = db.Column(db.String(20))
    veiculo = db.Column(db.String(50))
    disponivel = db.Column(db.Boolean, default=True)
    entregas = db.relationship('Pedido', backref='entregador', lazy=True)

class Pedido(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cliente_id = db.Column(db.Integer, db.ForeignKey('cliente.id'), nullable=False)
    entregador_id = db.Column(db.Integer, db.ForeignKey('entregador.id'))
    status = db.Column(db.String(20), default='pendente')
    endereco_entrega = db.Column(db.String(200), nullable=False)
    valor_total = db.Column(db.Float, nullable=False)
    data_pedido = db.Column(db.DateTime, default=db.func.current_timestamp())
    data_entrega = db.Column(db.DateTime)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
