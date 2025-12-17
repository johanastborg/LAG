from flask import Blueprint, jsonify

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def health_check():
    return jsonify({"status": "healthy", "service": "ERP Core"})
