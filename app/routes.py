from flask import Blueprint

main_bp = Blueprint('main', __name__)

@main_bp.route('/submit', methods=['GET', 'POST'])
def submit():
    return "<h3>Success: Request passed through the firewall cleanly!</h3>", 200