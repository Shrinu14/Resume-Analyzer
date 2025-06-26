import re
from dateutil import parser
from datetime import datetime

def detect_date_gaps(text: str, gap_months: int = 6) -> bool:
    """
    Detects if there are gaps > gap_months in experience/education.
    """
    dates = re.findall(r"\b(?:\d{4}|\d{2}/\d{4})\b", text)
    parsed_years = []

    for d in dates:
        try:
            year = parser.parse(d, fuzzy=True).year
            parsed_years.append(year)
        except:
            continue

    parsed_years = sorted(set(parsed_years))
    for i in range(1, len(parsed_years)):
        diff = parsed_years[i] - parsed_years[i-1]
        if diff >= (gap_months // 12) + 1:
            return True

    return False
