import os
os.chdir("natural_selection_sim-main/")
# Liste contenant l'ensemble des individus
liste = []
# Liste contenant l'ensemble de la nourriture
liste_food = []


# Fonctions permettant d'intéragir avec les listes
def add(liste, creature):
    liste.append(creature)
    
def len(liste):
    return len(liste)

def retirer(index, liste):
    del liste[index]

def clear(liste):
    liste = []