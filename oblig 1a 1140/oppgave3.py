#encoding: utf-8

# a)

# åpner filen
leser = open("in01.txt", "r", encoding="utf-8")
# leser filen
innhold = leser.read()


# b1)

# teller hvor mange ganger "er", i filen og lagrer i denne filen
antall = innhold.count("er")

# printer ut antall "er"-er
print(f"antall ganger \"er\" er skrevet: {antall}")

# lukker leseren
leser.close()


# b2)

# åpner og leser filen
leser = open("in01.txt", "r", encoding="utf-8")

# denne gangen leser vi med .split() methoden som gjør at innhold er en liste
innhold = leser.read().split()

# setter antall tilbake på null
antall = 0

# for loop for å finne antall som slutter med er
for ord in innhold:
    # bruker .endswith for å finne om det slutter på "er"
    if ord.endswith("er") == True:

        # øker antallet om det slutter med "er"
        antall += 1

# printer ut svaret
print(f'Antall tilfeller som slutter med \"er\" er: {antall}')

# lukker som vanlig
leser.close()


# c)

# samme som oppgavene før åpne og lese
leser = open("in01.txt", "r", encoding="utf-8")
innhold = leser.read().split()

# array som vi skal lagre ordene i
ending = []

# for loop
for ord in innhold:

    # tar de siste to bokstavene i hvert ord
    to_siste = ord[-2:]

    # legger de til endriger listen
    ending.append(to_siste)


# lager mellomrom mellom de to siste ordene og lager en streng fra de
streng = " ".join(ending)
print(streng)
leser.close()
