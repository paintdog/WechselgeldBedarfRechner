import pprint


euros = [200, 100, 50, 20, 10, 5, 2, 1]
cents = [50, 20, 10, 5, 2, 1]



beträge = [52.23]


summe_beträge = round(sum(beträge), 2)
summe_check   = 0                  # Ich prüfe hier später gegen, ob ich dieselbe Summe erhalte

# beträge = [56.12]

euro_bedarf = {euro : 0 for euro in euros}
cent_bedarf = {cent : 0 for cent in cents}

for betrag in beträge:

    # print(betrag)

    betrag_euro = int(betrag // 1)
    betrag_cent = int(str(betrag).split(".")[1])

    # Wir berechnen den Wechselgeldbedarf
    for euro in euros:
        if betrag_euro >= euro and betrag_euro > 0:
            euro_bedarf[euro] += int(betrag_euro // euro)
            betrag_euro -= (betrag_euro // euro) * euro

    for cent in cents:
        if betrag_cent >= cent and betrag_cent > 0:
            cent_bedarf[cent] += int(betrag_cent // cent)
            betrag_cent -= (betrag_cent // cent) * cent

# Wir geben den Wechselgeldbedarf aus
for euro in euros:
    # print("€", euro, euro_bedarf[euro], euro * euro_bedarf[euro])
    summe_check += euro * euro_bedarf[euro]
    if euro_bedarf[euro] == 0:
        pass
    elif euro >= 100:
        print(f"{euro} €-Schein  x {euro_bedarf[euro]: 4d} = {euro * euro_bedarf[euro] * 1.0:8.2f} €" )
    elif euro >= 10:
        print(f" {euro} €-Schein  x {euro_bedarf[euro]: 4d} = {euro * euro_bedarf[euro] * 1.0:8.2f} €" )
    elif euro >= 5:
        print(f"  {euro} €-Schein  x {euro_bedarf[euro]: 4d} = {euro * euro_bedarf[euro] * 1.0:8.2f} €" )
    elif euro >= 1:
        print(f"  {euro} €-Münze   x {euro_bedarf[euro]: 4d} = {euro * euro_bedarf[euro] * 1.0:8.2f} €" )

for cent in cents:
    # print(cent, cent_bedarf[cent], cent / 100 * cent_bedarf[cent])
    summe_check += cent / 100 * cent_bedarf[cent]
    if cent_bedarf[cent] == 0:
        pass
    elif cent >= 10:
        print(f" {cent} ¢-Münze   x {cent_bedarf[cent]: 4d} = {cent * cent_bedarf[cent] / 100:8.2f} €" )
    elif cent >= 1:
        print(f"  {cent} ¢-Münze   x {cent_bedarf[cent]: 4d} = {cent * cent_bedarf[cent] / 100:8.2f} €" )
    

assert summe_beträge, round(summe_check, 2) 
print(summe_beträge, round(summe_check, 2))
