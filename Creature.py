import pygame, constantes, random, queue

# Création des entités

class Creature(pygame.sprite.Sprite):
    
    def __init__(self, generation):
        # Appelle le init de la classe hérité
        super().__init__()
    
        self.alive = True # Définit le statut de l'individu (mort ou vif)
        self.generation = generation
    
        self.deplacement = random.randint(1, 15) # Variable qui donne le nombre de pixels parcouru à chaque déplacement
        self.size = random.uniform(0.75, 1.25) # Facteur varaiation de taille, multiplié à une base de 18 pixels de hauteur/largeur
        self.new_size = int(18*self.size) # Nouvelle taille
        self.speed = random.uniform(1, 2.25)*(2-self.size)
        self.food = 0 # Niveau de nourriture initial de l'individu
        self.view = random.randint(40, 90) # Capacitées optiques de l'individu
        
        self.image = pygame.transform.scale(pygame.image.load("assets/rubiks.png"), (self.new_size, self.new_size))
        self.rect = self.image.get_rect()
        
        
        
        self.max_x = int(constantes.LARGEUR_GENERAL - self.new_size) # Détermine la position x maximale pour rester dans la surface
        self.max_y = int(constantes.HAUTEUR_GENERAL - self.new_size) # Détermine la position y maximale pour rester dans la surface
        self.x = random.randint(self.new_size, self.max_x) # Donne une position en x qui se place dans la surface
        self.y = random.randint(self.new_size, self.max_y) # Donne une position en y qui se place dans la surface
        
        self.direction_x = random.choice([-1, 0, 1]) # Déplacement aléatoire en x soit en positif, soit en négatif, soit a l'arrêt
        self.direction_y = random.choice([-1, 0, 1]) # De même en y 
    
        
    def eat(self, x_food, y_food): # self --> creature | dimension (x,y) --> nourriture 
        if (x_food <= self.x + self.new_size and x_food >= self.x) and (y_food <= self.y + self.new_size and y_food >= self.y):
            self.food += 1
            return True
        else:
            return False

        
    # Déplacement: 
    def view_food(self): # Détermine si autour de la créature une nouriture est présente
        for food in queue.liste_food:
            if food.eat == False: # Si la nouriture n'a pas été mangé on regarde la distance euclidienne avec la créature 
                if ((food.x - self.x) ** 2 + (food.y - self.y) ** 2) ** 0.5 <= (self.size+self.view):
                    return True, food.x, food.y # On renvoie aussi les coordonnées de la nourriture pour en faire une target


    def move (self):

        luck= 25 # Probabilité de changer de direction 

        view_food_result = self.view_food() 

        # Déplace la créature dans la direction de la nourriture si elle est présente aux alentours

        if view_food_result !=None:
            view, x_food, y_food = self.view_food() # On stocke les différentes données

            if view==True:
                # Selon la position de la nourriture par rapport à la créature les calculs changent
                if x_food > self.x:
                    if x_food - self.x > int(self.speed * self.deplacement):
                        self.x += int(self.speed * self.deplacement)
                    else: self.x =x_food
    
                else: #x_food < self.x
                    if self.x - x_food > int(self.speed * self.deplacement):
                        self.x -= int(self.speed * self.deplacement)
                    else: self.x = x_food


                if y_food > self.y:
                    if y_food-self.y > int(self.speed * self.deplacement):
                        self.y += int(self.speed * self.deplacement)
                    else : self.y = y_food

                else: #y_food < self.y
                    if self.y - y_food > int(self.speed * self.deplacement):
                        self.y -= int(self.speed * self.deplacement)
                    else: self.y = y_food

        # Si il n'y a pas de nouriture proche il continu a se déplacé
        else:
            if random.random() <= luck / 100:
                self.direction_x = random.choice([-1, 0, 1])
                self.direction_y = random.choice([-1, 0, 1])

            self.x += self.direction_x * int(self.speed * self.deplacement)
            self.y += self.direction_y * int(self.speed * self.deplacement)
     
        # Vérifier si l'image est sortie de la surface
        if self.x < 0:
            self.x = self.new_size
        elif self.x > self.max_x:
            self.x = self.max_x
        if self.y < 0:
            self.y = self.new_size
        elif self.y > self.max_y:
            self.y = self.max_y

    # Vérifier les limites de la surface générale et empêcher les entitées de sortir
        if self.x < self.new_size:
            self.x = self.new_size
        elif self.x > self.max_x:
            self.x = self.max_x - self.new_size
        if self.y < self.new_size:
            self.y = self.new_size
        elif self.y > self.max_y:
            self.y = self.max_y - self.new_size
            
        self.last_x = self.x
        self.last_y = self.y
    
    
    def Clear(self):
        surface = pygame.Surface(self.image.get_size())
        surface.fill("white")
        
    def Afficher(self, fenetre):
        fenetre.blit(self.image, (self.x, self.y))


        
        
        
