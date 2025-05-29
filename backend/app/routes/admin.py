from flask import Blueprint, request, jsonify
from ..models import User
from ..utils.auth import admin_required
from .. import db

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/farmers/pending', methods=['GET'])
@admin_required
def get_pending_farmers():
    farmers = User.query.filter_by(role='farmer', is_approved=False).all()
    
    return jsonify({
        'farmers': [f.to_dict() for f in farmers]
    }), 200

@admin_bp.route('/farmers/<int:farmer_id>/approve', methods=['POST'])
@admin_required
def approve_farmer(farmer_id):
    farmer = User.query.filter_by(id=farmer_id, role='farmer').first()
    
    if not farmer:
        return jsonify({'error': 'Farmer not found'}), 404
    
    farmer.is_approved = True
    db.session.commit()
    
    return jsonify({
        'message': 'Farmer approved successfully',
        'farmer': farmer.to_dict()
    }), 200

@admin_bp.route('/farmers/<int:farmer_id>/reject', methods=['POST'])
@admin_required
def reject_farmer(farmer_id):
    farmer = User.query.filter_by(id=farmer_id, role='farmer').first()
    
    if not farmer:
        return jsonify({'error': 'Farmer not found'}), 404
    
    db.session.delete(farmer)
    db.session.commit()
    
    return jsonify({'message': 'Farmer rejected and removed'}), 200

@admin_bp.route('/farmers', methods=['GET'])
@admin_required
def get_all_farmers():
    farmers = User.query.filter_by(role='farmer').all()
    
    return jsonify({
        'farmers': [f.to_dict() for f in farmers]
    }), 200
