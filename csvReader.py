import csv
import sys

csv.field_size_limit(sys.maxsize)

#Lecture de fichier csv
def importCSV(fichier : str, separateur = ";"):
    tCSV = csv.DictReader(open(fichier,'r'), delimiter = separateur)
    return [ dict(ligneDuTableau) for ligneDuTableau in tCSV]

#Ecriture de fichier csv
def exportCSV(tableau : list, fichier : str):
    header = tableau[0].keys()
    fichierCSV = csv.DictWriter(open(fichier, 'w'), fieldnames = header)
    fichierCSV.writeheader()
    for ligne in tableau:
        try :
            fichierCSV.writerow(ligne)
        except IndexError:
            print("Le tableau est vide")
            break
    return None
