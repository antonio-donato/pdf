import docx

news = docx.Document("documento.docx")

sezioni = news.sections

print("Il documento contiene:")
print("{0} sezioni".format(len(sezioni)))

paragrafi = news.paragraphs
print ("{0} paragrafi".format(len(paragrafi)))

for p in paragrafi:
    print(p.text)
    print("-"*50)
