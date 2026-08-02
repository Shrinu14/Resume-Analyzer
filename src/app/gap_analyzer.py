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

    # Only whole years are extracted (no month resolution), so consecutive
    # entries a single year apart (e.g. 2020, 2021) are normal and NOT a
    # gap. The previous check flagged any diff >= 1 year as a gap, which is
    # true for nearly every resume with sequential dates and made this
    # signal meaningless. Require more than 1 year between entries, and
    # scale the threshold by gap_months so a larger gap_months requires a
    # bigger jump.
    min_gap_years = max(1, gap_months // 12) + 1
    for i in range(1, len(parsed_years)):
        diff = parsed_years[i] - parsed_years[i - 1]
        if diff >= min_gap_years:
            return True

    return False
