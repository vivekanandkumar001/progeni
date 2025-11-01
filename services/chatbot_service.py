import uuid, time

SESSION_STORE = {}  # in-memory, use Redis in prod

def start_chat(user_id, data):
    sid = f"sess_{uuid.uuid4().hex[:8]}"
    SESSION_STORE[sid] = {"user_id": user_id, "history": [], "created": time.time(), "meta": data}
    return sid

def chat_step(session_id, user_message):
    s = SESSION_STORE.get(session_id)
    if not s:
        return {"error":"session not found"}
    s['history'].append({"from":"user","text":user_message})
    # placeholder: integrate existing_core.chatbot_rag here
    reply = "Swami: (placeholder) — integrate OpenRouter/Groq here."
    s['history'].append({"from":"bot","text":reply})
    return {"reply": reply, "done": False}
