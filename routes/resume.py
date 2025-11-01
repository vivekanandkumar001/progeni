from flask import Blueprint, request, redirect, url_for, flash, render_template, session, current_app, send_from_directory
from models.user import db, ResumeRecord
from services.file_service import allowed_file, save_upload
from services.model_service import analyze_file
import os

resume_bp = Blueprint('resume', __name__, template_folder='../templates')

@resume_bp.route('/upload', methods=['POST'])
def upload():
    uid = session.get('user_id')
    if not uid:
        flash('Login required', 'warning'); return redirect(url_for('auth.login'))
    if 'resume' not in request.files:
        flash('No file uploaded', 'warning'); return redirect(url_for('main.dashboard'))
    f = request.files['resume']
    if f.filename == '':
        flash('No file selected', 'warning'); return redirect(url_for('main.dashboard'))
    if not allowed_file(f.filename):
        flash('File type not allowed', 'danger'); return redirect(url_for('main.dashboard'))
    name, path = save_upload(f, uid)
    try:
        result = analyze_file(path)
        score = None
        if isinstance(result, dict):
            score = result.get('score') or result.get('match_score')
        rec = ResumeRecord(filename=name, filepath=path, result=str(result), score=score, user_id=uid)
        db.session.add(rec); db.session.commit()
        flash('Analysis done', 'success')
        return redirect(url_for('resume.view', rid=rec.id))
    except Exception as e:
        current_app.logger.error("Analyze failed: %s", e)
        flash('Analysis failed', 'danger'); return redirect(url_for('main.dashboard'))

@resume_bp.route('/view/<int:rid>')
def view(rid):
    uid = session.get('user_id')
    rec = ResumeRecord.query.get_or_404(rid)
    if rec.user_id != uid:
        flash('Access denied', 'danger'); return redirect(url_for('main.dashboard'))
    return render_template('analyze_result.html', record=rec)

@resume_bp.route('/download/<path:filename>')
def download(filename):
    return send_from_directory(current_app.config['UPLOAD_FOLDER'], filename, as_attachment=True)
