import pygame, constantes, random

# Création des entités

class Creature(pygame.sprite.Sprite):
    
    def __init__(self):
        # Appelle le init de la classe hérité
        super().__init__()
    
        self.alive = True # Définit le statut de l'individu (mort ou vif)
    
        self.speed = random.uniform(1, 2.25)
        self.deplacement = random.randint(1, 15) # Variable qui donne le nombre de pixels parcouru à chaque déplacement
        self.size = random.uniform(0.75, 1.25) # Facteur varaiation de taille, multiplié à une base de 18 pixels de hauteur/largeur
        self.new_size = int(18*self.size) # Nouvelle taille
        self.food = 0 # Niveau de nourriture initial de l'individu
        self.view = 1 # Capacitées optiques de l'individu
        
        self.image = pygame.transform.scale(pygame.image.load("assets/rubiks.png"), (self.new_size, self.new_size))
        self.rect = self.image.get_rect()
        
        
        
        self.max_x = int(constantes.LARGEUR_GENERAL - self.new_size) # Détermine la position x maximale pour rester dans la surface
        self.max_y = int(constantes.HAUTEUR_GENERAL - self.new_size) # Détermine la position y maximale pour rester dans la surface
        self.x = random.randint(self.new_size, self.max_x) # Donne une positione en x qui se place dans la surface
        self.y = random.randint(self.new_size, self.max_y) # Donne une positione en y qui se place dans la surface
        self.last_x = self.x # Permet de conserver le dernier déplacement en x
        self.last_y = self.y # Permet de conserver le dernier déplacement en y
    
    
    def detect(self):
        return
        
    def eat(self, x_food, y_food): # self --> creature | dimension (x,y) --> nourriture 
        if (x_food <= self.x + self.new_size and x_food >= self.x) and (y_food <= self.y + self.new_size and y_food >= self.y):
            self.food += 1
            return True
        else:
            return False

        
    def move(self):
        self.x += random.randint(-int(self.speed * self.deplacement), int(self.speed * self.deplacement))
        self.y += random.randint(-int(self.speed * self.deplacement), int(self.speed * self.deplacement))
    # # Probabilité de changer de direction
    #     probability = 1
    #     if random.random() <= probability / 100:
    #         self.x = (self.last_x - self.deplacement)
    #         self.y = (self.last_y - self.deplacement)
        
    #     else:
    #         if random.randint(1, 2) == 1:
    #             self.x += random.randint(-int(self.speed * self.deplacement), int(self.speed * self.deplacement))
    #             self.y += random.randint(-int(self.speed * self.deplacement), int(self.speed * self.deplacement))
    #             self.last_x = self.x
    #             self.last_y = self.y
    #         else:
    #             self.x -= random.randint(-int(self.speed * self.deplacement), int(self.speed * self.deplacement))
    #             self.y -= random.randint(-int(self.speed * self.deplacement), int(self.speed * self.deplacement))
    #             self.last_x = self.x
    #             self.last_y = self.y
        

            
    # direction = random.choice(["gauche", "droite", "haut", "bas"])
    # if direction == "gauche":
    #     self.x -= self.deplacement * self.speed
    # elif direction == "droite":
    #     self.x += self.deplacement * self.speed
    # elif direction == "haut":
    #     self.y -= self.deplacement * self.speed
    # else:
    #     self.y += self.deplacement * self.speed

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


        
        
        
