
# åpner og leser
leser = open("in01.txt", "r", encoding="utf-8")
# bruker readlines for å lese linjer
linjer = leser.readlines()

# liste for å lagre listene
linjeList = []

# forloop for å loope gjennom linjene
for linje in linjer:
    # legger til linjene i listen
    linjeList.append(linje.split())

# counter variabler
linjer = 0
ord = 0

# forloop for å telle antall linjer
for ant_linje in linjeList:
    linjer += 1

    # forloop inni forloop for å telle ord
    for ant_ord in ant_linje:
        ord += 1

# print
print(f"Antall ord: {ord}")
print(f"Antall linjer: {linjer}")

leser.close()
