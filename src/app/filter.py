from typing import List, Dict

def filter_resumes(resume_scores: List[Dict], min_score: int = 60, required_skills: List[str] = []) -> List[Dict]:
    """
    Filters resumes based on total score and required skills.
    """
    filtered = []

    for r in resume_scores:
        if r["total_score"] < min_score:
            continue
        if required_skills:
            if not set(required_skills).issubset(set(r.get("skills", []))):
                continue
        filtered.append(r)

    return filtered
