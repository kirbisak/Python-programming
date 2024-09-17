import os

def read():
  lst = []
  with open("anonymizacia/udaje.txt", "r") as f:
    for line in f:
      lst.append(line.replace("\n", ""))
  return lst

with open("anonymizacia/dokument.txt", "r") as f1:
    with open("anonymizacia/dokument_anonym.txt", "w") as f2:
        doc = f1.read()
        temp = read()
        for i in temp:
            doc.replace(i, "****")
        f2.write(doc)
