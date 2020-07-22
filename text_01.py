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
cartella = "D:\\Github_repository\\Wingesfar"
#"C:\\Workspace_git\\Wingesfar"
stringSearch = "56821C"
stringSub = "Python!!!"
contatore = 0
trovati = 0
errori = 0

#listaFile = os.listdir(cartella)

for nomeFile in os.listdir(cartella):
    valore = os.path.isfile(os.path.join(cartella, nomeFile))

    if os.path.isfile(os.path.join(cartella, nomeFile)) and nomeFile.upper().endswith(".CBL"):
        # print('file: {0}'.format(nomeFile))

        fileInput = open(os.path.join(cartella, nomeFile), "rt", encoding="cp1252")

        try:
            data = fileInput.read()
            data1 = data.replace(stringSearch, stringSub)
            if data != data1:
                print(data1)
                trovati += 1
            fileInput.close()

            fileOut = open(os.path.join(cartella, nomeFile), "wt")
            fileOut.write(data1)
            fileOut.close()

            contatore += 1

        except:
            print("Errore file su {0}".format(fileInput))

            errori += 1

print("Elaborati {0} File".format(contatore))
print("Sostituiti {0} File".format(trovati))
print("Errori {0}".format(errori))
