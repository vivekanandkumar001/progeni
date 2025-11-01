# app.py
from flask import Flask, render_template, redirect, url_for
from config import Config
from models.user import db

def create_app():
    app = Flask(__name__, static_folder='static', template_folder='templates')
    app.config.from_object(Config)
    db.init_app(app)

    with app.app_context():
        # ensure instance dir exists and create tables
        import os
        os.makedirs(app.instance_path, exist_ok=True)
        db.create_all()

    @app.route('/')
    def index():
        return render_template('index.html')

    return app

# For local debug only (HF will use gunicorn CMD)
if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=7860, debug=True)
