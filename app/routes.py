from flask import Blueprint, render_template # Added render_template here!
from app.waf.telemetry import telemetry_warehouse

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return render_template('index.html')

@main_bp.route('/submit', methods=['GET', 'POST'])
def submit():
    return "<h3>Success: Request passed through the firewall cleanly!</h3>", 200

@main_bp.route('/admin/dashboard')
def dashboard():
    logs_list = telemetry_warehouse.logs

    total_attacks = len(logs_list)

    return render_template(
        'dashboard.html', 
        logs=logs_list, 
        total_attacks=total_attacks
    )