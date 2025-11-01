import logging


MODEL = None

def init_model():
    global MODEL
    if MODEL is None:
        try:
            from existing_core.model import load_model
            MODEL = load_model()
        except Exception:
            try:
                from model import load_model
                MODEL = load_model()
            except Exception as e:
                logging.warning("Model loader not found: %s", e)
                MODEL = None
    return MODEL

def analyze_file(filepath):
    init_model()
    try:
        from existing_core.model import analyze_resume
        return analyze_resume(filepath, MODEL)
    except Exception:
        try:
            from model import analyze_resume
            return analyze_resume(filepath, MODEL)
        except Exception as e:
            return {"error":"Model not configured: " + str(e)}
