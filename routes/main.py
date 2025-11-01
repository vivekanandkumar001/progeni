from flask import Blueprint, render_template, session, redirect, url_for
from models.user import User, ResumeRecord
main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    if session.get('user_id'):
        return redirect(url_for('main.dashboard'))
    return render_template('index.html')

@main_bp.route('/dashboard')
def dashboard():
    uid = session.get('user_id')
    if not uid:
        return redirect(url_for('auth.login'))
    user = User.query.get(uid)
    resumes = ResumeRecord.query.filter_by(user_id=uid).order_by(ResumeRecord.created_at.desc()).all()
    return render_template('dashboard.html', user=user, resumes=resumes)
