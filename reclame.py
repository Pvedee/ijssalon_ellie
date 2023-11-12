from algemene_functies import mijn_functie_2

# Hier wordt de aanbieding berekend
def aanbieding_1(smaak, prijs, korting): 
    reclame = (prijs * (1 - korting))
    return (f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van € {prijs:.2f} voor € {reclame:.2f}")
        # omrekenen naar 2 decimalen gevonden via datasciencepartners.nl/f-strings-python/
  
print (aanbieding_1("aardbei", 4 , 0.1))


# Het berekenen van inkomsten en BTW
def inkomsten_totaal(inkomsten, btw):
    totaal = sum(inkomsten)  # SUM gevonden op ioflood.com/blog/python-sum-list-how-to-calculate-the-sum-of-the-elements-in-a-list/
    btw = (totaal * btw)
    return (f"Het totaal van alle inkomsten van deze week is € {totaal:.2f}, waarover € {btw:.2f} btw betaald dient te worden.")

inkomsten = [220, 430, 125, 160, 205, 90, 345]
print (inkomsten_totaal(inkomsten, 0.09))


# Laagste en Hoogste bedrag
def laag_en_hoog(mijn_lijst):
    hoogste = max(mijn_lijst) 
    laagste = min(mijn_lijst)
    return (hoogste, laagste)

mijn_lijst = inkomsten
print (laag_en_hoog(mijn_lijst))



# Gemiddelde bereken
def gemiddelde(mijn_lijst):
    avarage = (sum(inkomsten) / 7)
    return (f"De gemiddelde inkomsten deze week zijn € {avarage:.2f}.")
print (gemiddelde(mijn_lijst))



# Meervoudig via hoog en laag
def meervoudig(invoer_lijst):
    return (laag_en_hoog(invoer_lijst))

invoer_lijst = [10,5,3,2,1,2,9]
print (meervoudig(invoer_lijst))



# Combinatie is mij helaas niet gelukt om op te lossen. 
# Ik kom niet uit de argumenten voor de invoer_lijst_2
''' def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    uitvoer = mijn_functie_2 (korte_lijst[0], korte_lijst[1])
    return uitvoer

invoer_lijst_2 = ???? 
print (combinatie(invoer_lijst_2))  '''

