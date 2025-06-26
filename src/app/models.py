from pydantic import BaseModel
from typing import List, Optional

class ResumeInput(BaseModel):
    file_path: str
    file_type: str  # "pdf", "docx", "png", etc.

class JDInput(BaseModel):
    jd_text: str

class ScoringInput(BaseModel):
    resume_text: str
    jd_text: str
    resume_skills: List[str]
    jd_skills: List[str]
    structure_score: int
    grammar_issues: List[str]
    has_gap: bool
    has_quantified_achievements: bool

class ScoreOutput(BaseModel):
    skill_match_score: float
    semantic_similarity_score: float
    structure_score: float
    language_score: float
    gap_score: float
    achievement_score: float
    total_score: float

class ResumeMetadata(BaseModel):
    candidate_name: Optional[str]
    skills: List[str]
    entities: dict
    score: ScoreOutput
