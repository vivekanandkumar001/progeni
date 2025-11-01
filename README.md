# PROGENI_FLASK

Flask migration of Progeni AI — resume analyzer + AI interviewer scaffold.

## Quick start (local)
1. Copy `.env` and edit secrets.
2. python -m venv venv
3. source venv/bin/activate  # or venv\Scripts\activate on Windows
4. pip install -r requirements.txt
5. python app.py
6. Open http://127.0.0.1:5000

## Deploy to Hugging Face Spaces (Docker)
- Ensure Dockerfile present and HF Space is Docker type.
- Push repo to HF Space; set Secrets in Space settings (OPENROUTER_API_KEY, SECRET_KEY).
