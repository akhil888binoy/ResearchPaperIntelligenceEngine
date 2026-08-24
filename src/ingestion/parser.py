from pypdf import PdfReader

reader = PdfReader('AttendanceandLeaveGuidelines.pdf')

for page in reader.pages:
    text = page.extract_text()
    print(text)
