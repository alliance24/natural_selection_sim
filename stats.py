import stockage

# statut de la simulation
statut = "Réglages" # Réglages, En cours, Terminé

generation = 0 # Numéro de la génération
nb_individus_start = 0 # Nombre d'individus au tout début de la simulation 
births = 0 # Nombre de naissances sur le nouveau tour 
nb_individus_alive =len(stockage.liste_individus) # Nombre d'individus qui ont survécu à la dernière génération
nb_individus_dead = 0 # Nombre d'individu qui n'ont pas survécu à la dernière génération
nb_individus_dead_total = 0 # Nombre d'individus morts depuis le début de la simulation 

# Définition des moyennes 
individus_moyenne_size = 0
individus_moyenne_view = 0
individus_moyenne_speed = 0

# Fonctions calculant les moyennes
def moyenne_size():
    count = 0
    sum = 0
    for individu in stockage.liste_individus:
        if individu.alive == True:
            count += 1
            sum += individu.new_size
    return round(sum/count, 1)

def moyenne_view():
    count = 0
    sum = 0
    for individu in stockage.liste_individus:
        if individu.alive == True:
            count += 1
            sum += individu.view
    return round(sum/count, 1)

def moyenne_speed():
    count = 0
    sum = 0
    for individu in stockage.liste_individus:
        if individu.alive == True:
            count += 1
            sum += individu.speed
    return round(sum/count, 1)


    
         
