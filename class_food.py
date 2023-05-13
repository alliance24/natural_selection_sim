import pygame
import random
import constantes


class Food():
    def __init__(self,):
        self.image=pygame.transform.scale(pygame.image.load("assets/Rond_rouge.png"), (14, 14))
        self.rect = self.image.get_rect()
        self.eat=False
        self.max_x = int(constantes.LARGEUR_GENERAL)
        self.max_y = int(constantes.HAUTEUR_GENERAL)
        self.x = random.randint(14, self.max_x)
        self.y = random.randint(14, self.max_y)
        

    # def spawn(self):
    #     # if self.x < 0:
    #     #     self.x = 18
    #     # elif self.x > self.max_x:
    #     #     self.x = self.max_x
    #     # if self.y < 0:
    #     #     self.y = 18
    #     # elif self.y > self.max_y:
    #     #     self.y = self.max_y
            
    #     self.x = random.randint(0, self.max_x)
    #     self.y = random.randint(0, self.max_y)


    def Afficher(self, fenetre):
        fenetre.blit(self.image, (self.x, self.y))
        pygame.display.update()


    