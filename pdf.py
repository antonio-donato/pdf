import PyPDF2

pdfFile1 = open("Auto Moretti - Donato - Francoforte - 15-17 maggio 2019.pdf", "rb")

reader1 = PyPDF2.PdfFileReader(pdfFile1)

pdfFile2 = open("test.pdf", "wb")
writer1 = PyPDF2.PdfFileWriter()

pag_0 = reader1.getPage(0)

writer1.addPage(pag_0)
writer1.addPage(pag_0)
writer1.addPage(pag_0)

writer1.write(pdfFile2)

numPage = reader1.numPages
print(numPage)

pdfFile1.close()
pdfFile2.close()

pdfFile2 = open("test.pdf", "rb")
reader2 = PyPDF2.PdfFileReader(pdfFile2)

numPage = reader2.numPages
print(numPage)

pdfFile2.close()
