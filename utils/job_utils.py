from .embedding_utils import cosine_sim
def top_k_matches(resume_embedding, jobs, k=3):

    scored = []
    for job in jobs:
        emb = job.get('embedding')
        if emb is None: continue
        
        sim = cosine_sim(resume_embedding, emb)
        scored.append((sim, job))
    scored.sort(reverse=True, key=lambda x: x[0])
    return [{"score": s, "job": j} for s,j in scored[:k]]
