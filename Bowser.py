import pygame

class Bowser():
    def __init__(self, image, x,y):
        self.dis = pygame.image.load(image)
        self.x = x                        
        self.y = y
        self.collision = 0                      
        self.rect = self.dis.get_rect(center = (self.x,self.y)) # creo un rettangolo intorno all'oggetto
    def disegna(self, screen):
        screen.blit(self.dis,self.rect)

    def check_collision(self,other_rect): 
        """controllo la collisione con il personaggio
        """
    
        if other_rect.colliderect(self.rect):
            self.collision = 1

        return self.collision
        