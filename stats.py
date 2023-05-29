import queue

generation = 0
nb_individus_start = 0 #nombre d'individu au tout début de la simulation 
births = 0 #nombre de naissance sur le nouveau tour 
nb_individus_alive =len(queue.liste_individus) #nombre d'individu qui ont survécue a la dernière génération
nb_individus_dead = 0 #Nombre d'individu qui n'ont pas survécu a la dernière génération
nb_individus_dead_total = 0 #Nombre d'individue mort depuis le début de la simulation 

individus_moyenne_size = 0
individus_moyenne_view = 0
individus_moyenne_speed = 0

        
def moyenne_size():
    count = 0
    sum = 0
    for individu in queue.liste_individus:
        if individu.alive == True:
            count += 1
            sum += individu.new_size
    return round(sum/count, 1)

def moyenne_view():
    count = 0
    sum = 0
    for individu in queue.liste_individus:
        if individu.alive == True:
            count += 1
            sum += individu.view
    return round(sum/count, 1)

def moyenne_speed():
    count = 0
    sum = 0
    for individu in queue.liste_individus:
        if individu.alive == True:
            count += 1
            sum += individu.speed
    return round(sum/count, 1)


    
         
