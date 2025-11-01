import os
from flask import Flask, render_template
from config import Config
from models.user import db
from routes import register_blueprints

def create_app():
    app = Flask(__name__, static_folder='static', template_folder='templates')
    app.config.from_object(Config)

    db.init_app(app)

    with app.app_context():
        os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
        os.makedirs('instance', exist_ok=True)
        db.create_all()

    register_blueprints(app)

    @app.route('/')
    def index():
        return render_template('index.html')

    return app


if __name__ == "__main__":
    app = create_app()
    # port 5000 for local dev; HF Dockerfile uses 7860
    app.run(host='0.0.0.0', port=int(os.getenv("PORT", 5000)), debug=True)
