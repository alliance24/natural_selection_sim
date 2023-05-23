import pygame

class Button():
    def __init__(self, screen):
        self.etat_click = False
        self.x = 0
        self.y = 0
        self.image = pygame.transform.scale(pygame.image.load("assets/start_button_troll.png"), (200, 200))
        self.rect = self.image.get_rect()



# mouse = pygame.mouse.get_pos()

#     if ev.type == pygame.MOUSEBUTTONDOWN:
        
#         #if the mouse is clicked on the
#         # button the game is terminated
#         if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40:
#             pygame.quit()
				
	
# 	# stores the (x,y) coordinates into
# 	# the variable as a tuple
	
	
# 	# if mouse is hovered on a button it
# 	# changes to lighter shade
# 	if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40:
# 		pygame.draw.rect(screen,color_light,[width/2,height/2,140,40])
		
# 	else:
# 		pygame.draw.rect(screen,color_dark,[width/2,height/2,140,40])
	
# 	# superimposing the text onto our button
# 	screen.blit(text , (width/2+50,height/2))
	
