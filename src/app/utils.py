import os

def infer_file_type(file_path: str) -> str:
    """
    Infers file type from file extension.
    """
    ext = os.path.splitext(file_path)[1].lower()
    return ext.strip('.')

def clean_text(text: str) -> str:
    """
    Remove extra spaces, newlines, and normalize text.
    """
    return " ".join(text.split())

def normalize_skills(skills: list) -> list:
    """
    Lowercase and strip skill names.
    """
    return list(set([s.lower().strip() for s in skills]))
