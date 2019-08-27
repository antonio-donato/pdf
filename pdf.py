import PyPDF2

pdfFile1 = open("C:\\Users\\antonio.donato\\Google Drive\\G3 Shared\\Travel\\Old\\56219783.pdf", "rb")

reader1 = PyPDF2.PdfFileReader(pdfFile1)

pdfFile2 = open("c:\\test.pdf", "wb")
