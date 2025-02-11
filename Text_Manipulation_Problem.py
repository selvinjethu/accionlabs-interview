import re
class TextExtraction:
    def extract(self, text):
        return re.findall(r"[a-zA-Z0-9]+[a-zA-Z0-9]+\\[a-zA-Z0-9], text")
    
text = "Emails, user@example.com"
extractor = TextExtraction()
print(extractor.extract_emails(text))