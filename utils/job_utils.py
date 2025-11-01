def top_k_matches(resume_embedding, jobs, k=3):
    # jobs: list of dicts with 'embedding' key
    scored = []
    for job in jobs:
        emb = job.get('embedding')
        if emb is None: continue
        # assume numpy array pickled; compute cosine
        import numpy as np
        from utils.embedding_utils import cosine_sim
        sim = cosine_sim(resume_embedding, emb)
        scored.append((sim, job))
    scored.sort(reverse=True, key=lambda x: x[0])
    return [{"score": s, "job": j} for s,j in scored[:k]]
