from pypdf import PdfReader

def extractAllPdfs(archiveList):
    pdfs = []
    pdfCount = 0
    for archive in archiveList:
        reader = PdfReader(archive)
        number_of_pages = len(reader.pages)
        page = reader.pages[0]
        pdfs.append(page.extract_text())
    return pdfs