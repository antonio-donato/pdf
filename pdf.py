import PyPDF2
import tkinter as tk
from tkinter import filedialog
from tkinter import *
from functools import partial
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
numeroPages = reader1.numPages

#window
tkWindow = Tk()
tkWindow.geometry('400x150')
tkWindow.title('Scegli la pagina da salvare')

#Label
usernameLabel = Label(tkWindow, text='Scegli una pagina da 1 a %d' % numeroPages).grid(row=2, column=0)
# selected = IntVar()
selected = StringVar()

usernameEntry = Entry(tkWindow, textvariable=selected).grid(row=2, column=2)

def clicked():
    print(selected.get())

#ok button
# okButton = Button(tkWindow, text="OK").grid(row=4, column=0)

tkWindow.mainloop()  #TODO Perchè non va oltre?

#chiedo dove salvare il file finale di una sola pagina
file_path_saved = filedialog.asksaveasfilename()

pdfFile2 = open(file_path_saved, "wb")
writer1 = PyPDF2.PdfFileWriter()

selectedNumPage = IntVar()
selectedNumPage = selected
# for numeroPagina in range(reader1.numPages):
writer1.addPage(reader1.getPage(selectedNumPage - 1))
#
# # print(reader1.getDocumentInfo().title)
#
writer1.write(pdfFile2)
#
pdfFile1.close()
pdfFile2.close()
