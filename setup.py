from setuptools import setup, find_packages

setup(
    name="resume-parser-nlp",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "spacy",
        "pdfplumber",
        "python-docx",
        "phonenumbers",
        "email-validator"
    ],
    entry_points={
        "console_scripts": [
            "resume-parser=main:main"
        ]
    }
)
