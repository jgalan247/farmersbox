from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..models import Product, User
from ..utils.auth import farmer_required
from .. import db

products_bp = Blueprint('products', __name__)

@products_bp.route('/', methods=['GET'])
@farmer_required
def get_products():
    user_id = get_jwt_identity()
    products = Product.query.filter_by(farmer_id=user_id).all()
    
    return jsonify({
        'products': [p.to_dict() for p in products]
    }), 200

@products_bp.route('/', methods=['POST'])
@farmer_required
def create_product():
    user_id = get_jwt_identity()
    data = request.get_json()
    
    # Validate required fields
    required_fields = ['name', 'price', 'unit']
    for field in required_fields:
        if field not in data:
            return jsonify({'error': f'{field} is required'}), 400
    
    product = Product(
        name=data['name'],
        description=data.get('description', ''),
        price=data['price'],
        unit=data['unit'],
        quantity_available=data.get('quantity_available', 0),
        is_available=data.get('is_available', True),
        farmer_id=user_id
    )
    
    db.session.add(product)
    db.session.commit()
    
    return jsonify({
        'message': 'Product created successfully',
        'product': product.to_dict()
    }), 201

@products_bp.route('/<int:product_id>', methods=['PUT'])
@farmer_required
def update_product(product_id):
    user_id = get_jwt_identity()
    product = Product.query.filter_by(id=product_id, farmer_id=user_id).first()
    
    if not product:
        return jsonify({'error': 'Product not found'}), 404
    
    data = request.get_json()
    
    # Update fields
    if 'name' in data:
        product.name = data['name']
    if 'description' in data:
        product.description = data['description']
    if 'price' in data:
        product.price = data['price']
    if 'unit' in data:
        product.unit = data['unit']
    if 'quantity_available' in data:
        product.quantity_available = data['quantity_available']
    if 'is_available' in data:
        product.is_available = data['is_available']
    
    db.session.commit()
    
    return jsonify({
        'message': 'Product updated successfully',
        'product': product.to_dict()
    }), 200

@products_bp.route('/<int:product_id>', methods=['DELETE'])
@farmer_required
def delete_product(product_id):
    user_id = get_jwt_identity()
    product = Product.query.filter_by(id=product_id, farmer_id=user_id).first()
    
    if not product:
        return jsonify({'error': 'Product not found'}), 404
    
    db.session.delete(product)
    db.session.commit()
    
    return jsonify({'message': 'Product deleted successfully'}), 200
