import language_tool_python

tool = language_tool_python.LanguageTool('en-US')

def analyze_language(text: str) -> list:
    """
    Returns a list of detected language/grammar issues.
    """
    matches = tool.check(text)
    issues = [match.message for match in matches]
    return issues[:10]  # limit to top 10 issues
