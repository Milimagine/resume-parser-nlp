from parser.file_loader import extract_text
from parser.extractor import parse_resume

def main():
    filepath = "examples/sample_resume.pdf"
    text = extract_text(filepath)
    data = parse_resume(text)
    
    for key, value in data.items():
        print(f"{key.capitalize()}: {value}")

if __name__ == "__main__":
    main()
