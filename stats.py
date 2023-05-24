import queue
# from queue import liste_individus
# from queue import liste_food


class Statistiques():
    
    def __init__(self):
        self.nb_individus_start = 0 #nombre d'individu au tout début de la simulation 
        self.births = 0 #nombre de naissance sur le nouveau tour 
        self.nb_individus_total = self.nb_individus_start + self.births #nombre d'induvidu total depuis le début de la simulation
        #self.nb_individus_alive =self.nb_individus_start #nombre d'individu qui ont survécue a la dernière génération
        self.nb_individus_dead = 0 #Nombre d'individu qui n'ont pas survécu a la dernière génération
        # self.nb_individus_dead_total = self.nb_individus_total - self.nb_individus_alive #Nombre d'individue mort depuis le début de la simulation 
        
        
    def moyenne_size(self):
        for individu in queue.liste_individus:
            count = 0
            sum = 0
            if individu.alive == True:
                count += 1
                sum += individu.size
        return sum/count
    
    def moyenne_view(self):
        for individu in queue.liste_individus:
            count = 0
            sum = 0
            if individu.alive == True:
                count += 1
                sum += individu.size
        return sum/count
    
    
    
    
         
