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
                self.rect.centerx += 30
            case 2: #left
                self.rect.centerx -= 30
            case 3: #up
                self.rect.centery += 30
            case 4: #down
                self.rect.centery -= 30
        

    def movement_limits(self, screen_width):
        #############################
        ## LIMITI MOVIMENTI BOWSER ###
        #############################
        #scorrimento infinito a sx
        if self.rect.right <= 0: 
                self.rect.right = screen_width-1
        # scorrimento a dx infinito
        if self.rect.right >= screen_width:
                self.rect.left = 1
        #mario non puo andare sotto il pavimento
        if self.rect.bottom >= self.y + self.rect.height/2 +1:
                self.rect.centery = self.y 
        #mario non puo uscire da sopra        
        if self.rect.top <=0:
                self.rect.top = 0