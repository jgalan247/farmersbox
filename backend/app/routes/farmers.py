from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..models import User
from .. import db

farmers_bp = Blueprint('farmers', __name__)

@farmers_bp.route('/profile', methods=['GET'])
@jwt_required()
def get_profile():
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    
    if not user or user.role != 'farmer':
        return jsonify({'error': 'Farmer not found'}), 404
    
    return jsonify({'farmer': user.to_dict()}), 200

@farmers_bp.route('/profile', methods=['PUT'])
@jwt_required()
def update_profile():
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    
    if not user or user.role != 'farmer':
        return jsonify({'error': 'Farmer not found'}), 404
    
    data = request.get_json()
    
    # Update allowed fields
    if 'farm_name' in data:
        user.farm_name = data['farm_name']
    if 'phone' in data:
        user.phone = data['phone']
    if 'address' in data:
        user.address = data['address']
    if 'latitude' in data:
        user.latitude = data['latitude']
    if 'longitude' in data:
        user.longitude = data['longitude']
    
    db.session.commit()
    
    return jsonify({
        'message': 'Profile updated successfully',
        'farmer': user.to_dict()
    }), 200