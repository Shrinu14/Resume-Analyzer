# app/scorer.py

from typing import List, Dict

def calculate_score(
    skill_match: float,           # 0.0 - 1.0
    semantic_similarity: float,   # 0.0 - 1.0
    structure_score: int,         # 0 - 10
    grammar_issues: List[str],    # List of issues
    has_gap: bool,                # True if gaps exist
    has_quantified_achievements: bool  # True if bullet points contain numbers
) -> Dict[str, float]:
    """
    Returns a breakdown + total score out of 100.
    """

    score_breakdown = {
        "skill_match_score": round(skill_match * 30, 2),
        "semantic_similarity_score": round(semantic_similarity * 20, 2),
        "structure_score": structure_score,  # 0–10
        "language_score": max(0, 10 - len(grammar_issues)),  # 0–10
        "gap_score": 10 if not has_gap else 5,  # penalty if gaps
        "achievement_score": 10 if has_quantified_achievements else 5
    }

    score_breakdown["total_score"] = round(sum(score_breakdown.values()), 2)
    return score_breakdown
