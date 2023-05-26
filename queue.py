# Fichier contenant les listes, les variables ainsi que les fonctions pour agir sur les listes
nb_individus = 25



# Liste contenant l'ensemble des individus
liste_individus = []
# Liste contenant l'ensemble de la nourriture
liste_food = []


# Fonctions permettant d'intéragir avec les listes
def add(liste, e):
    liste.append(e)
    
def len(liste):
    return len(liste)

def clear(liste):
    liste = []