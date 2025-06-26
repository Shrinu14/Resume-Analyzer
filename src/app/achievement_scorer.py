import re

def has_quantified_achievements(text: str) -> bool:
    """
    Checks if the resume contains metrics or quantifiable achievements.
    Looks for numbers in bullet points or action phrases.
    """
    # Regex: bullet point lines with numbers/percent
    quantified = re.findall(r"[\u2022\-•\*] .*?\d+[%]?", text)
    return len(quantified) >= 2
