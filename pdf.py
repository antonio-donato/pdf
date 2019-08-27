import PyPDF2

pdfFile1 = open("Auto Moretti - Donato - Francoforte - 15-17 maggio 2019.pdf", "rb")

reader1 = PyPDF2.PdfFileReader(pdfFile1)

pdfFile2 = open("test.pdf", "wb")
writer1 = PyPDF2.PdfFileWriter()

for numeroPagina in range(reader1.numPages):
    writer1.addPage(reader1.getPage(numeroPagina))

writer1.write(pdfFile2)

pdfFile1.close()
pdfFile2.close()

