import pygame
from pygame._sdl2.video import Window, Renderer, Texture
import cfg

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
        self.fontsize = 25
        self.playerName = ""
        self.gettingPlayer = True
        
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
        """chiude la finestra e libera la memoria
        """
        super().destroy()

    def playsound(self):
        pygame.mixer.pre_init(22050, 16, 2, 8192)
        pygame.mixer.music.load('MUSIC/You Got a Moon.mp3')
        pygame.mixer.music.play(-1)
        pygame.event.wait()

    def disegnaschermo(self):
        """disegna tutti gli elementi della finestra
        """
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

            ## chiedo inserimento del nome utente
            while self.gettingPlayer:
                self.playerName = self.input_player_name()[1]
                # print("ci siamo " + self.playerName)
                self.gettingPlayer=False
                
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

            # gestione uscita dal gioco in fase di scelta
            if (event.type == pygame.KEYDOWN and event.key ==  pygame.K_ESCAPE):
                pygame.quit()

    def aggiorna(self):
        """aggiorna lo schermo
        """
        pygame.display.update()

    def draw_text(self,phrase,x,y, color):
        """disegna una label sullo schermo

        Args:
            word (_type_): _description_
            x (_type_): _description_
            y (_type_): _description_

        Returns:
            _type_: _description_
        """
        font = pygame.font.SysFont(self.font, self.fontsize)
        text = font.render("{}".format(phrase), True, color)
        return self.screen.blit(text,(x,y))

    def input_player_name(self):
        """chiede il nome dell'utente

        Returns:
            _type_: la scritta con il nome [0] e il nome stesso [1]
        """
        word=""
        question = "Inserisci il tuo nome : "
        self.draw_text(question,300,400, (255,255,255)) #example asking name
        pygame.display.flip()
        done = True
        while done:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
    
                # leggo qualsiasi lettera per formare il nome
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        word+=str(chr(event.key))
                    if event.key == pygame.K_b:
                        word+=chr(event.key)
                    if event.key == pygame.K_c:
                        word+=chr(event.key)
                    if event.key == pygame.K_d:
                        word+=chr(event.key)
                    if event.key == pygame.K_e:
                        word+=chr(event.key)
                    if event.key == pygame.K_f:
                        word+=chr(event.key)
                    if event.key == pygame.K_g:
                        word+=chr(event.key)
                    if event.key == pygame.K_k:
                        word+=chr(event.key)
                    if event.key == pygame.K_h:
                        word+=chr(event.key)
                    if event.key == pygame.K_j:
                        word+=chr(event.key)
                    if event.key == pygame.K_i:
                        word+=chr(event.key)
                    if event.key == pygame.K_l:
                        word+=chr(event.key)
                    if event.key == pygame.K_m:
                        word+=chr(event.key)
                    if event.key == pygame.K_n:
                        word+=chr(event.key)
                    if event.key == pygame.K_o:
                        word+=chr(event.key)
                    if event.key == pygame.K_p:
                        word+=chr(event.key)
                    if event.key == pygame.K_q:
                        word+=chr(event.key)
                    if event.key == pygame.K_r:
                        word+=chr(event.key)
                    if event.key == pygame.K_s:
                        word+=chr(event.key)
                    if event.key == pygame.K_t:
                        word+=chr(event.key)
                    if event.key == pygame.K_u:
                        word+=chr(event.key)
                    if event.key == pygame.K_v:
                        word+=chr(event.key)
                    if event.key == pygame.K_w:
                        word+=chr(event.key)
                    if event.key == pygame.K_y:
                        word+=chr(event.key)
                    if event.key == pygame.K_z:
                        word+=chr(event.key)
                    if event.key == pygame.K_1:
                        word+=chr(event.key)
                    if event.key == pygame.K_2:
                        word+=chr(event.key)
                    if event.key == pygame.K_3:
                        word+=chr(event.key)
                    if event.key == pygame.K_4:
                        word+=chr(event.key)
                    if event.key == pygame.K_5:
                        word+=chr(event.key)
                    if event.key == pygame.K_6:
                        word+=chr(event.key)
                    if event.key == pygame.K_7:
                        word+=chr(event.key)
                    if event.key == pygame.K_8:
                        word+=chr(event.key)
                    if event.key == pygame.K_9:
                        word+=chr(event.key)

                    # mi fermo quando premo return 
                    if event.key == pygame.K_RETURN:
                        done=False
    
        return self.draw_text(word,300 + len(question)* self.fontsize / 1.5 ,400, (255,0,0)), word