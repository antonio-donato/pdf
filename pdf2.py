import PyPDF2
from os import listdir
import os

# file in folder
listaFile = listdir()

# open write pdf merger file
nomeFileDestinazione = input()
PDF_Destinazione = open(nomeFileDestinazione, "wb")
merger = PyPDF2.PdfFileMerger()


for nomeFile in listaFile:
    if os.path.isfile(nomeFile) and nomeFile.upper().endswith(".PDF"):
        pdfFile = open(nomeFile, "rb")
        readerPDF = PyPDF2.PdfFileReader(pdfFile)
        merger.append(readerPDF)
        pdfFile.close()

merger.write(PDF_Destinazione)
PDF_Destinazione.close()
