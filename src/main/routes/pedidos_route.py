from flask import Blueprint, jsonify, request

from src.main.composer import register_pedido_composer, find_pedidos_composer, update_pedido_composer
from src.main.adapter import flask_adapter

pedido_route_bp = Blueprint('pedidos', __name__)


@pedido_route_bp.route('/', methods=['GET'])
def ok():
    return jsonify({'msg': 'ok'}), 200


@pedido_route_bp.route('/register_pedido', methods=['POST'])
def register_pedido():
    response = flask_adapter(request=request, api_route=register_pedido_composer())
    
    message = {
        'type': 'Pedidos',
        'data': response.body.__dict__
    }
    
    return jsonify(message), response.status_code


@pedido_route_bp.route('/find_pedidos', methods=['POST'])
def find_pedidos():
    response = flask_adapter(request=request, api_route=find_pedidos_composer())

    message = {
        'type': 'Pedidos',
        'data': [item.__dict__ for item in response.body]
    }
    
    return jsonify(message), response.status_code


@pedido_route_bp.route('/update_pedidos', methods=['PUT'])
def update_pedidos():
    response = flask_adapter(request=request, api_route=update_pedido_composer())

    message = {
        'type': 'Pedidos',
        'data': response.body.__dict__
    }

    return jsonify(message), response.status_code
