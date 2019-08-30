import os
print("Digita il percorso della cartella da valutare:")
# cartella = input()

print()
print("Digita la stringa da cercare:")
# stringSearch = input()

print()
print("Digita la nuova stringa da sostituire:")
# stringSub = input()

# solo per test
cartella = "C:\\Workspace_git\\Wingesfar"
stringSearch = "56821C"
stringSub = "PIPPOOOO!!!"
contatore = 0
errori = 0

#listaFile = os.listdir(cartella)

for nomeFile in os.listdir(cartella):
    valore = os.path.isfile(os.path.join(cartella, nomeFile))

    if os.path.isfile(os.path.join(cartella, nomeFile)) and nomeFile.upper().endswith(".CBL"):
        print('file: {0}'.format(nomeFile))

        fileInput = open(os.path.join(cartella, nomeFile), "rt", encoding="cp1252")

        try:
            data = fileInput.read()
            data.replace(stringSearch, stringSub)
            fileInput.close()

            fileOut = open(os.path.join(cartella, nomeFile), "wt")
            fileOut.write(data)
            fileOut.close()

            contatore += 1

        except:
            print("Errore file su {0}".format(fileInput))

            errori += 1

print("Elaborati {0} File".format(contatore))
print("Errori {0}".format(errori))
