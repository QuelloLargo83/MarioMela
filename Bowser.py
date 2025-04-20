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
    
    def random_move(self, dir):
        """gestione movimento casuale di bowser
        """
        match dir:
            case 1: #right
                self.rect.centerx += 10
            case 2: #left
                self.rect.centerx -= 10
            case 3: #up
                self.rect.centery +=10
            case 4: #down
                self.rect.centery -=10