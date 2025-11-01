from .main import main_bp
from .auth import auth_bp
from .resume import resume_bp
from .interview import interview_bp
from .notify import notify_bp

def register_blueprints(app):
    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(resume_bp, url_prefix='/resume')
    app.register_blueprint(interview_bp, url_prefix='/interview')
    app.register_blueprint(notify_bp, url_prefix='/notify')
