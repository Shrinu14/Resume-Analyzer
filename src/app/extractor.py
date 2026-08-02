# app/extractor.py

import spacy
from spacy.matcher import PhraseMatcher
from typing import List
from src.app.skills_list import SKILL_KEYWORDS

# Load SpaCy English model
nlp = spacy.load("en_core_web_sm")

def extract_skills(text: str) -> List[str]:
    doc = nlp(text.lower())

    # Phrase matcher for known skill keywords
    matcher = PhraseMatcher(nlp.vocab, attr="LOWER")
    patterns = [nlp(skill) for skill in SKILL_KEYWORDS]
    # spaCy 3.x API: PhraseMatcher.add(key, patterns, *, on_match=None).
    # The old v2-style call `matcher.add("SKILLS", None, *patterns)` raises a
    # TypeError on spaCy 3.x and broke every /analyze/ request.
    matcher.add("SKILLS", patterns)

    matches = matcher(doc)
    skills = set([doc[start:end].text for _, start, end in matches])

    return list(skills)

def extract_named_entities(text: str) -> dict:
    doc = nlp(text)
    entities = {"ORG": [], "PERSON": [], "GPE": [], "EDUCATION": []}

    for ent in doc.ents:
        if ent.label_ in entities:
            entities[ent.label_].append(ent.text)

    return entities
