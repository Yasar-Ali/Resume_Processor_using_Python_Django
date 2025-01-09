import re
import pdfplumber
from docx import Document

class ResumeParser:
    def __init__(self, file):
        self.file = file
        self.content = self._extract_text()
    
    def _extract_text(self):
        """Extract text from PDF or DOCX file"""
        file_extension = self.file.name.split('.')[-1].lower()
        
        if file_extension == 'pdf':
            return self._extract_from_pdf()
        elif file_extension in ['docx', 'doc']:
            return self._extract_from_docx()
        else:
            raise ValueError("Unsupported file format. Please upload PDF or DOCX file.")
    
    def _extract_from_pdf(self):
        """Extract text from PDF file"""
        with pdfplumber.open(self.file) as pdf:
            return "\n".join(page.extract_text() for page in pdf.pages)
    
    def _extract_from_docx(self):
        """Extract text from DOCX file"""
        doc = Document(self.file)
        return "\n".join(paragraph.text for paragraph in doc.paragraphs)
    
    def extract_email(self):
        """Extract email address from text"""
        email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        emails = re.findall(email_pattern, self.content)
        return emails[0] if emails else None
    
    def extract_phone(self):
        """Extract phone number from text"""
        phone_pattern = r'(?:\+\d{1,3}[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}'
        phones = re.findall(phone_pattern, self.content)
        return phones[0] if phones else None
    
    def extract_first_name(self):
        """Extract first name from text"""
        lines = self.content.split('\n')
        for line in lines[:10]:  # Check first 10 lines for name
            words = line.strip().split()
            if len(words) >= 1:
                # Assume first word that's not a title is a first name
                for word in words:
                    if word.lower() not in ['mr', 'mrs', 'ms', 'dr', 'prof']:
                        return word
        return None