import pygame
from pygame._sdl2.video import Window, Renderer, Texture

class OptionChooser(Window):
    """classe per gestione schermata iniziale opzioni
    """

    def __init__(self, screen, bg, choiceimg, p1image, p2image, font, fontcolor):
        super().__init__
        self.ret_scelta = 1 # default scelta mario
        self.running = 1
        self.screen = screen
        self.font = font
        self.fontcolor = fontcolor
        self.sfondo = pygame.image.load(bg)
        self.sceltaimg = pygame.image.load(choiceimg)
        
        # carico i personaggi per la scelta sulla finestra iniziale
        self.personaggio1 = pygame.image.load(p1image)
        self.personaggio2 = pygame.image.load(p2image)

        self.h1 = self.personaggio1.get_height()

        # calcolo posizioni per immagine scelta
        self.hscreen = self.sfondo.get_height()
        self.wscreen = self.sfondo.get_width()
        self.screencenter = (self.wscreen//2 ,self.hscreen//2)

        # disegno i rettangoli intorno ai personaggi e li posiziono rispetto al centro del bg
        self.p1_rect = self.personaggio1.get_rect( center= (self.screencenter[0], self.screencenter[1]))
        self.p2_rect = self.personaggio2.get_rect( center= (self.screencenter[0], self.h1 + 50 + self.screencenter[1]))

        # posiziono subito la scelta di fianco al primo personaggio
        self.scelta_rect = self.sceltaimg.get_rect(center = (self.p1_rect.centerx +  70 , self.p1_rect.centery))

    def destroy(self):
        super().destroy()

    def playsound(self):
        pygame.mixer.pre_init(22050, 16, 2, 8192)
        pygame.mixer.music.load('MUSIC/You Got a Moon.mp3')
        pygame.mixer.music.play(-1)
        pygame.event.wait()

    def disegnaschermo(self):
        self.screen.blit(self.sfondo, (0,0))
        # self.playsound()

        # disegno i personaggi per la scelta 
        self.screen.blit(self.personaggio1, self.p1_rect)
        self.screen.blit(self.personaggio2, self.p2_rect)

        # disegno l'immagine della scelta
        self.screen.blit(self.sceltaimg,self.scelta_rect)
        
        # scrivo cosa fare
        myFont = pygame.font.SysFont(self.font, 36)
        Label_ScegliPers = myFont.render('SCEGLI IL PERSONAGGIO', 1, self.fontcolor)
        self.screen.blit(Label_ScegliPers, (self.p1_rect.centerx, self.p1_rect.centery - self.personaggio1.get_height()))   
    
        ##################################
        #  GESTIONE EVENTI DEI PULSANTI  #
        ##################################
        for event in pygame.event.get():

            ## muovo l'immagine della scelta del personaggio
            if (event.type == pygame.KEYDOWN and event.key == pygame.K_UP):
                self.scelta_rect.centery = self.p1_rect.centery
            if (event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN):
                self.scelta_rect.centery = self.p2_rect.centery

            ## alla pressione di RETURN esco e raccolgo le scelte
            if (event.type == pygame.KEYDOWN and event.key ==  pygame.K_RETURN):
            
                ## gestione scelta del personaggio
                match self.scelta_rect.centery:
                
                    case self.p1_rect.centery: 
                        self.ret_scelta = 1
                
                    case self.p2_rect.centery: 
                        self.ret_scelta = 2

                ## chiudo la finestra
                self.running = 0
                self.destroy()

    ## aggiorna lo schermo
    def aggiorna(self):
        pygame.display.update()