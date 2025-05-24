from parser.extractor import parse_resume

def test_parse_resume():
    sample_text = "John Doe\nEmail: john.doe@example.com\nPhone: (123) 456-7890"
    result = parse_resume(sample_text)
    assert result["name"] == "John Doe"
    assert result["email"] == "john.doe@example.com"
    assert "+11234567890" in result["phone"]
