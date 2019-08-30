import os
print("Digita il percorso della cartella da valutare:")
cartella = input()

print()
print("Digita la stringa da cercare:")
stringSearch = input()

print()
print("Digita la nuova stringa da sostituire:")
stringSub = input()

#listaFile = os.listdir(cartella)

for nomeFile in os.listdir(cartella):
    valore = os.path.isfile(os.path.join(cartella, nomeFile))

    if os.path.isfile(os.path.join(cartella, nomeFile)) and nomeFile.upper().endswith(".CBL"):
        print('file: {0}'.format(nomeFile))

        fileInput = open(os.path.join(cartella, nomeFile), "rt")
        data = fileInput.read()
        data.replace(stringSearch, stringSub)
        fileInput.close()

        #fileInput = fileInput.replace(stringSearch, stringSub)
        fileOut = open(os.path.join(cartella, nomeFile), "wt")
        fileOut.write(data)
        fileOut.close()
