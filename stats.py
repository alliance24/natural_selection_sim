import queue
from queue import liste
from queue import liste_food


class Statistiques():
    
    def __init__(self):
        self.nb_individus_start = 0
        self.nb_individus_end = 0
        self.nb_individus_dead = self.nb_individus_start - self.nb_individus_end
        self.births = 0
        self.food_proportion = None
        self.individus_per_round = [[], []]
        
        
    def moyenne_size(self):
        for individu in liste:
            count = 0
            sum = 0
            if individu.alive == True:
                count += 1
                sum += individu.size
        return sum/count
    
    
    
    
         
