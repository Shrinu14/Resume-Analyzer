import re

ESSENTIAL_SECTIONS = ["education", "experience", "skills", "projects"]
OPTIONAL_SECTIONS = ["certifications", "achievements", "summary"]

def check_resume_structure(text: str) -> int:
    """
    Returns a score (0–10) based on presence of required sections.
    """
    text_lower = text.lower()
    present = [section for section in ESSENTIAL_SECTIONS if section in text_lower]
    optional = [section for section in OPTIONAL_SECTIONS if section in text_lower]

    score = len(present) * 2  # 4 required sections × 2 = 8 max
    score += min(len(optional), 2)  # Bonus 2 pts max for optional sections

    return min(score, 10)
