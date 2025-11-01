import os, uuid
from werkzeug.utils import secure_filename
from flask import current_app

ALLOWED_EXTENSIONS = {'pdf', 'docx', 'doc', 'txt'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def save_upload(file_storage, user_id):
    folder = current_app.config['UPLOAD_FOLDER']
    os.makedirs(folder, exist_ok=True)
    filename = secure_filename(file_storage.filename)
    unique_name = f"{user_id}_{uuid.uuid4().hex}_{filename}"
    path = os.path.join(folder, unique_name)
    file_storage.save(path)
    return unique_name, path
