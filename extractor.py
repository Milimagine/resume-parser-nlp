import re
import phonenumbers
from email_validator import validate_email, EmailNotValidError
import spacy
from .text_cleaner import clean_text

nlp = spacy.load("en_core_web_sm")

def extract_email(text):
    emails = re.findall(r"\S+@\S+", text)
    for email in emails:
        try:
            valid = validate_email(email)
            return valid.email
        except EmailNotValidError:
            continue
    return None

def extract_phone(text):
    for match in phonenumbers.PhoneNumberMatcher(text, "US"):
        return phonenumbers.format_number(match.number, phonenumbers.PhoneNumberFormat.E164)
    return None

def extract_name(text):
    doc = nlp(text)
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            return ent.text
    return None

def parse_resume(text):
    cleaned = clean_text(text)
    return {
        "name": extract_name(cleaned),
        "email": extract_email(cleaned),
        "phone": extract_phone(cleaned),
    }

