# Fichier contenant les listes, les variables ainsi que les fonctions pour agir sur les listes
nb_individus = 20  # Nombre d'individu 
facteur_food = 150 # Facteur de nourriture
time_generation = 15 # Durée d'une génération (par défaut sur 15s)
timer = 15 # Timer de la génération, affiche les secondes en temps réel, par défaut sur 15
nb_boucles = 20 * time_generation # Permet de trouver le nombre de fois ou la boucle principale est jouée (20 car 20fps)

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