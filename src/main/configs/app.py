from flask import Flask
from flask_cors import CORS
from src.main.routes import pedido_route_bp


app = Flask(__name__)
CORS(app)

app.register_blueprint(pedido_route_bp)
