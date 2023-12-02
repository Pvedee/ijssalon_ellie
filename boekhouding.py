from helper import *
from presentatie import * 
import csv

inkomsten = {
    "Aardbeien-ijs-totaal" : 1000,
    "Vanille-ijs-totaal":2000,
    "Chocolade-ijs-totaal":1500,
    "Waterijsjes-totaal":750
    }

totaal_inkomsten = som(inkomsten)

def presenteer(inkomsten, totaal_inkomsten):
    for k, v in inkomsten.items():
        print (k, ": €", v)
        print (20 * "=")
        print (f"Totaal : €", som({v}))

with open('boekhouding.csv', 'w', newline='') as csvfile:
    for key, value in inkomsten.items():
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerow([key,value])


