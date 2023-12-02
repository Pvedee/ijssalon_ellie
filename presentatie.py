def presenteer(d={}, totaal=""):
    mijn_dict = {
        "vis" : 10, 
        "vlees": 25, 
        "overig" : 15
        }
  
    totaal = 50
       
    for k, v in mijn_dict.items():
        print (k, ": €", v)
        print (16 * "=")
        print (f"Totaal : € {totaal}")

