from flask import Blueprint, request, jsonify, session
from services.chatbot_service import start_chat, chat_step

interview_bp = Blueprint('interview', __name__)

@interview_bp.route('/start', methods=['POST'])
def start():
    uid = session.get('user_id')
    data = request.json or {}
    session_id = start_chat(uid, data)
    return jsonify({"session_id": session_id})

@interview_bp.route('/step', methods=['POST'])
def step():
    data = request.json or {}
    session_id = data.get('session_id')
    user_msg = data.get('message')
    resp = chat_step(session_id, user_msg)
    return jsonify(resp)
