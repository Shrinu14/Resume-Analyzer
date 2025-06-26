# app/matcher.py

from sentence_transformers import SentenceTransformer, util
from typing import Tuple

# Load model once at module level
model = SentenceTransformer("all-MiniLM-L6-v2")

def calculate_similarity(resume_text: str, jd_text: str) -> float:
    """
    Compute semantic similarity between resume and job description text.
    Returns a float between 0 and 1.
    """
    if not resume_text or not jd_text:
        return 0.0

    embeddings = model.encode([resume_text, jd_text], convert_to_tensor=True)
    score = util.cos_sim(embeddings[0], embeddings[1])
    return round(float(score), 4)

def compare_skills_overlap(resume_skills: list, jd_skills: list) -> float:
    """
    Calculates skill overlap ratio (set intersection / JD skills).
    """
    if not jd_skills:
        return 0.0

    matched = set(resume_skills).intersection(set(jd_skills))
    return round(len(matched) / len(jd_skills), 4)
