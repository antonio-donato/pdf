import PyPDF2
import tkinter as tk
from tkinter import filedialog
import os

root = tk.Tk()
root.withdraw()

# File PDF da aprire
file_path = filedialog.askopenfilename()
# devo aggiungere gli apici altrimenti non me lo apre
file_path_complete = '"' + file_path + '"'

#apertura file
os.system(file_path_complete)

pdfFile1 = open(file_path, "rb")

reader1 = PyPDF2.PdfFileReader(pdfFile1)

#chiedo dove salvare il file finale di una sola pagina
file_path_saved = filedialog.asksaveasfilename()

pdfFile2 = open(file_path_saved, "wb")
writer1 = PyPDF2.PdfFileWriter()

for numeroPagina in range(reader1.numPages):
    writer1.addPage(reader1.getPage(0))

# print(reader1.getDocumentInfo().title)

writer1.write(pdfFile2)

pdfFile1.close()
pdfFile2.close()
