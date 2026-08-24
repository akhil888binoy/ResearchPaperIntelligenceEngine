from pypdf import PdfReader

reader = PdfReader('docs/AttendanceandLeaveGuidelines.pdf')
def splitter(n, s):
    pieces = s.split()
    return (" ".join(pieces[i:i+n]) for i in range(0, len(pieces), n))


def parser():
    for page in reader.pages:
        print(page)
        text = page.extract_text()
        for piece in splitter(1000, text):
            print(piece)
