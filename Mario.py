import pygame

class Mario():
    def __init__(self, image, x,y):
        self.x = x
        self.y = y
        self.xInit = x # mem coordinate iniziali
        self.yInit = y # mem coordinate iniziali
        self.gameImage = pygame.image.load(image)
        self.Image = image
        self.rect = self.gameImage.get_rect(center = (self.x,self.y)) # creo un rettangolo intorno all'oggetto
        self.gameImageFlip = pygame.transform.flip(self.gameImage,True,False) # personaggio girato 

    def disegna (self, screen):
        """disegna il personaggio sullo schermo

        Args:
            screen (_type_): _description_
        """
        screen.blit(self.gameImage,self.rect)
    
    def reInit(self, gameImage):
        self.x = self.xInit
        self.y = self.yInit
        self.gameImage = gameImage
        self.rect = self.gameImage.get_rect(center = (self.x,self.y))
        self.gameImageFlip = pygame.transform.flip(self.gameImage,True,False) # personaggio girato 
        
        return self.rect, self.gameImageFlip
    
    def rePositionInit(self):
        self.x = self.xInit
        self.y = self.yInit
    
    def disegna_flip(self, screen):
        screen.blit(self.gameImageFlip,self.rect)
    
    def loadImage(self, image):
        self.gameImage = pygame.image.load(image)
    
    def movement_limits(self, screen_width):
        """ limita i movimenti del personaggio dinamicamente

        Args:
            screen_width (_type_): dimensione dello schermo
        """
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
    
    def getMarioRect(self):
        return self.rect
    
    def getMarioFlip(self):
        self.gameImageFlip = pygame.transform.flip(self.gameImage,True,False) # Mario girato a sx
        return self.gameImageFlip
    
    def setPosition(self,x,y):
        self.rect.centerx = x
        self.rect.centery = y