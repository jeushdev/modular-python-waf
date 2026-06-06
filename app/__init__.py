from app.waf.middleware import WAFMiddleware
from flask import Flask
from app.routes import main_bp

def create_app():
    app = Flask(__name__)

    app.secret_key = 'super_secret_admin_key_change_this_later'

    app.register_blueprint(main_bp)

    WAFMiddleware(app)

    return app