# Resume Parser NLP

An NLP-powered resume parser that extracts name, email, and phone number from resumes in PDF or DOCX format.

## Features

- Extracts name using spaCy's NER
- Validates and extracts email
- Parses phone numbers using `phonenumbers`
- Supports PDF and DOCX resumes

## Installation

```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
