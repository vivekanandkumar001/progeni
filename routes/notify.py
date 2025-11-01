from flask import Blueprint, request, jsonify
from services.notify_service import send_email_stub

notify_bp = Blueprint('notify', __name__)

@notify_bp.route('/email', methods=['POST'])
def email():
    data = request.json or {}
    send_email_stub(data)
    return jsonify({"status":"sent"})
