from flask import Blueprint, jsonify
from ..models import User, Product

public_bp = Blueprint('public', __name__)

@public_bp.route('/farms', methods=['GET'])
def get_public_farms():
    # Only return approved farmers with their locations
    farmers = User.query.filter_by(role='farmer', is_approved=True).all()
    
    farms = []
    for farmer in farmers:
        # Get available products count
        products_count = Product.query.filter_by(
            farmer_id=farmer.id,
            is_available=True
        ).count()
        
        farms.append({
            'id': farmer.id,
            'farm_name': farmer.farm_name,
            'farmer_name': farmer.name,
            'latitude': farmer.latitude,
            'longitude': farmer.longitude,
            'address': farmer.address,
            'phone': farmer.phone,
            'products_count': products_count
        })
    
    return jsonify({'farms': farms}), 200

@public_bp.route('/farms/<int:farm_id>/products', methods=['GET'])
def get_farm_products(farm_id):
    farmer = User.query.filter_by(id=farm_id, role='farmer', is_approved=True).first()
    
    if not farmer:
        return jsonify({'error': 'Farm not found'}), 404
    
    products = Product.query.filter_by(farmer_id=farm_id, is_available=True).all()
    
    return jsonify({
        'farm': {
            'id': farmer.id,
            'farm_name': farmer.farm_name,
            'farmer_name': farmer.name,
            'phone': farmer.phone,
            'address': farmer.address
        },
        'products': [p.to_dict() for p in products]
    }), 200


