import pygame

class Bowser():
    def __init__(self, image, x,y, InitMov):
        self.dis = pygame.image.load(image)
        self.x = x                        
        self.y = y
        self.Xinit = x # mem posizione iniziale
        self.Yinit = y # mem posizione iniziale
        self.collision = 0
        self.InitMov = InitMov
        self.InitMovMem = InitMov # mem init mov                     
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
                self.rect.centerx += self.InitMov
            case 2: #left
                self.rect.centerx -= self.InitMov
            case 3: #up
                self.rect.centery += self.InitMov
            case 4: #down
                self.rect.centery -= self.InitMov
        

    def movement_limits(self, screen_width):
        """impone movimenti limitati a bowser nello schermo

        Args:
            screen_width (_type_): larghezza schermo
        """
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
    
    def reinitMovDisplacement(self):
        """reset range movimento bowser
        """
        self.InitMov = self.InitMovMem
    
    def mangia_mela(self, mele_array, _mela_sound):
        """definisce cosa succede quando bowser mangia una mela

        Args:
            mele_array (array of mela obj): array con le mele create a schermo
            _mela_sound (pygame.sound): suono da riprodurre alla collisione
        """
        for i in range(len(mele_array)):
            if mele_array[i].attrib != '':      # ho inizializzato vuoto quindi quando viene assegnato qualcosa è l'id della mela che ha generata la collisione
                idx_mela_collisione = i     # appoggio id della mela che ha generato collisione
        
        del mele_array[idx_mela_collisione]   # cancello solo la mela che ha generato la collisione  
                   
        _mela_sound.play()         # suono
        self.InitMov += 2          # aumenta la velocita di movimento di bowser