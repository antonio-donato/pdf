import os
print("Digita il percorso della cartella da valutare:")
cartella = input()

print()
print("Digita la stringa da cercare:")
stringSearch = input()

print()
print("Digita la nuova stringa da sostituire:")
stringSub = input()

listaFile = os.listdir(cartella)

for nomeFile in listaFile:
    # fileDestinazione = open("C:/Workspace_git/Wingesfar/donant-testXXXX.cbl", "wt")
    fileInput = open(nomeFile).read()
    fileInput = fileInput.replace(stringSearch, stringSub)
    fileOut = open(nomeFile, "wt")
    fileOut.write(fileInput)
    fileOut.close()

#with open("C:/Workspace_git/Wingesfar/gesm0010.cbl", "rt") as myfile:
#    for myline in myfile:
#
#        if myline.find("WG-2703") != -1:
#            myline = myline.replace("WG-2703", "CIAONE!")
#
#        fileDestinazione.writelines(myline)
#
#fileDestinazione.close()
