def decoreer(tekst=""):
    tekst="header"
    lengte = len(tekst) + 4
    print()
    print(lengte * "*")
    print(f"* {tekst} *")
    print(lengte * "*")
    print()


def fooi_pp(bedrag, personen): 
    bedrag_per_persoon = bedrag / personen
    return (f"Het bedrag per persoon is € {bedrag_per_persoon:.2f} ")


def onderstreep(tekst=""):
    uit = []
    uit.append(tekst) 
    uit.append(len(tekst) * "=")
    return uit

def som(totaal={}):
    return sum(totaal.values())


#print (som(totaal={}))  #test-verder hier van geen waarde.