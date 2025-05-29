from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_jwt_extended import JWTManager

db = SQLAlchemy()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    
    # Load config
    from .config import Config
    app.config.from_object(Config)
    
    # Initialize extensions
    db.init_app(app)
    CORS(app, origins=['http://localhost:5173', 'http://localhost:3000'])
    jwt.init_app(app)
    
    # Register blueprints
    from .routes.auth import auth_bp
    from .routes.farmers import farmers_bp
    from .routes.products import products_bp
    from .routes.admin import admin_bp
    from .routes.public import public_bp
    
    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(farmers_bp, url_prefix='/api/farmers')
    app.register_blueprint(products_bp, url_prefix='/api/products')
    app.register_blueprint(admin_bp, url_prefix='/api/admin')
    app.register_blueprint(public_bp, url_prefix='/api/public')
    
    # Create tables
    with app.app_context():
        db.create_all()
        # Create default super admin if not exists
        from .models import User
        admin = User.query.filter_by(email='admin@honestybox.com').first()
        if not admin:
            admin = User(
                email='admin@honestybox.com',
                name='Super Admin',
                role='super_admin',
                is_approved=True
            )
            admin.set_password('admin123')
            db.session.add(admin)
            db.session.commit()
    
    return app
