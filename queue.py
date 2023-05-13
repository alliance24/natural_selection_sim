import os
os.chdir("natural_selection_sim-main/")
liste = []
liste_food = []

def add(liste, creature):
    liste.append(creature)
    
def len(liste):
    return len(liste)

def retirer(index, liste):
    del liste[index]

def clear(liste):
    liste = []