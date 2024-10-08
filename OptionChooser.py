import pygame
from pygame._sdl2.video import Window, Renderer, Texture

class OptionChooser(Window):

    def __init__(self, screen, sfondo):
        super().__init__
        self.running = 1
        self.screen = screen
        self.sfondo = pygame.image.load(sfondo)

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
        
        ## chiudo la finestra
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key ==  pygame.K_RETURN:
                self.running = 0
                self.destroy()

    ## aggiorna lo schermo
    def aggiorna(self):
        pygame.display.update()