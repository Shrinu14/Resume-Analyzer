from src.app.parser import extract_text
from src.app.extractor import extract_skills, extract_named_entities
from src.app.jd_parser import extract_required_skills
from src.app.matcher import calculate_similarity, compare_skills_overlap
from src.app.structure_checker import check_resume_structure
from src.app.language_check import analyze_language
from src.app.gap_analyzer import detect_date_gaps
from src.app.achievement_scorer import has_quantified_achievements
from src.app.scorer import calculate_score
from src.app.chat_feedback import get_resume_feedback
from src.app.utils import clean_text, normalize_skills

def analyze_resume_pipeline(resume_path: str, file_type: str, jd_text: str) -> dict:
    # 1. Extract resume text
    resume_text = extract_text(resume_path, file_type)
    resume_text = clean_text(resume_text)

    # 2. Extract skills & named entities
    resume_skills = normalize_skills(extract_skills(resume_text))
    named_entities = extract_named_entities(resume_text)

    # 3. Parse JD
    jd_skills = normalize_skills(extract_required_skills(jd_text))

    # 4. Compute similarity scores
    semantic_score = calculate_similarity(resume_text, jd_text)
    skill_overlap = compare_skills_overlap(resume_skills, jd_skills)

    # 5. Run checks
    structure_score = check_resume_structure(resume_text)
    grammar_issues = analyze_language(resume_text)
    has_gap = detect_date_gaps(resume_text)
    has_metrics = has_quantified_achievements(resume_text)

    # 6. Final score breakdown
    score = calculate_score(
        skill_match=skill_overlap,
        semantic_similarity=semantic_score,
        structure_score=structure_score,
        grammar_issues=grammar_issues,
        has_gap=has_gap,
        has_quantified_achievements=has_metrics
    )

    # 7. Optional: LLM-based resume feedback
    suggestions = get_resume_feedback(resume_text)

    return {
        "resume_skills": resume_skills,
        "jd_skills": jd_skills,
        "named_entities": named_entities,
        "grammar_issues": grammar_issues,
        "structure_score": structure_score,
        "has_gap": has_gap,
        "has_metrics": has_metrics,
        "score_breakdown": score,
        "llm_suggestions": suggestions
    }
