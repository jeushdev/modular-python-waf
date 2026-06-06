from app.waf.middleware import WAFMiddleware
from flask import Flask

def create_app():
    app = Flask(__name__)

    app.secret_key = 'super_secret_admin_key_change_this_later'

    WAFMiddleware(app)

    return app