# existing_core/model.py
def load_model():
    # Replace with actual model load logic (transformers, sentence-transformers, etc.)
    print("Stub model load")
    return {"model":"stub"}

def analyze_resume(path, model=None):
    # Replace with actual analyze logic.
    # Return consistent dict: {score: float, top_jobs: [...], suggestions: {...}}
    return {"message": f"Analyzed (stub) {path}", "score": 0.55, "top_jobs": []}
