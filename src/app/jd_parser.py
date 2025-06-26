# app/jd_parser.py

from typing import List
from src.app.extractor import extract_skills
from src.app.skills_list import SKILL_KEYWORDS

def extract_required_skills(jd_text: str) -> List[str]:
    """
    Extract relevant skills mentioned in the job description text.
    """
    jd_skills = extract_skills(jd_text)
    
    # Optional: augment with keywords that appear in both JD and predefined list
    highlighted = [skill for skill in SKILL_KEYWORDS if skill in jd_text.lower()]
    
    # Combine and deduplicate
    all_skills = list(set(jd_skills + highlighted))
    return all_skills
