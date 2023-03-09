# a)

# åpner og leser
leser = open("in01.txt", "r", encoding="utf-8")
fil = leser.read().split()

# lager liste
tekstListe = []
tekstListe.append(fil)
# print(tekstListe)

# forloop for å slitte hvert ord
for ord in tekstListe:
    # printer de
    print("\n".join(ord))


leser.close()
