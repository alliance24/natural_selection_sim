import os
os.chdir("natural_selection_sim-main/")
liste = []

def append(creature):
    liste.append(creature)
    
def len(liste):
    return len(liste)

def retirer(index, liste):
    del liste[index]

def clear(liste):
    liste = []