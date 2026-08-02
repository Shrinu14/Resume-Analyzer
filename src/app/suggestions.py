# app/suggestions.py
#
# NOTE: kept for backwards compatibility / potential future use; the main
# pipeline uses chat_feedback.get_resume_feedback(). Uses the same
# non-crashing pattern as chat_feedback.py so an unreachable LLM backend
# doesn't raise if this ever gets wired in.
from src.app.chat_feedback import get_resume_feedback, FALLBACK_MESSAGE  # noqa: F401


def get_resume_improvement_tips(resume_text: str) -> str:
    return get_resume_feedback(resume_text)
