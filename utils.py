import re

def normalize_whitespace(text):
    """Remove extra spaces, newlines, and tabs from text."""
    return re.sub(r'\s+', ' ', text.strip())

def is_valid_name(name):
    """
    Heuristically checks if a string could be a valid name.
    You can expand this with more rules or ML models later.
    """
    if not name:
        return False
    if len(name.split()) > 4 or len(name) < 3:
        return False
    if any(char.isdigit() for char in name):
        return False
    return True

def extract_lines(text):
    """Splits text into lines, removes empty ones, and strips them."""
    return [line.strip() for line in text.splitlines() if line.strip()]

def get_first_non_empty_line(text):
    """Returns the first non-empty line from the text."""
    lines = extract_lines(text)
    return lines[0] if lines else None

def find_section(text, keywords):
    """
    Attempts to locate a section of a resume by looking for common keywords.
    Returns the start index of the section.
    """
    lines = extract_lines(text)
    for i, line in enumerate(lines):
        for keyword in keywords:
            if keyword.lower() in line.lower():
                return i
    return None
