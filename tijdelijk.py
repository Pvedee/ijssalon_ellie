from helper import decoreer

def print_aanbieding():
    prijzen = {
    "aardbei"    :   3,
    "vanille"    :   4,
        "chocolade" :   5
        }

    aanbieding = prijzen["aardbei"] * 0.8   # De variable Vanille omgewisseld voor aardbei   

    reclame_tekst = f"Vandaag in de aanbieding: vanille-ijs, 1 liter - slechts € {aanbieding}"

    reclame_tekst2 = reclame_tekst[:63]

    # print (reclame_tekst2)

    reclame_tekst3 = (reclame_tekst2) . upper()

    # print (reclame_tekst3)

    reclame_tekst4 = reclame_tekst3 . split()

    # print (reclame_tekst4)



    for el in reclame_tekst4:
        # print (el)
        # print (el . lower()) 

        if len(el) > 5: 
            print (el . upper())  # geeft alleen woorden met 5 karakters weer
        else: 
            print (el . lower ())

decoreer("Aanbieding")
print_aanbieding()

