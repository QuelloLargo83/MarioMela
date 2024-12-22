import os
import sys
import random
import math


#########################################
## check del sistema su cui sta girando #
#########################################
SYSTEM: str
if "linux" in sys.platform: SYSTEM = "Linux"
elif "win32" in sys.platform: SYSTEM = "Windows"
elif "darwin" in sys.platform: SYSTEM = "MacOs"
else: SYSTEM = "Other"

match SYSTEM:    
    case "Linux":
        bars = '/'
    case "Windows":
        bars = '\\'
    case "MacOs":
        bars = '/'
    case _:
        bars = '/'

########################################
############# IMPOSTAZIONI #############
########################################
FPS = 60
TIMER_meleSet = 1000        # millisecondi intervallo di apparizione mele
TIMER_giocoSet = 1000       # velocita tempo di gioco
MAX_TIME = 120             # timeout gioco
MARIO_X_INIT = 100
MARIO_Y_INIT = 973
left = False                # parto con mario girato a dx
VEL_grav = 2
MARIO_SPEED = 0.01
MARIO_ANGLE = random.uniform(0, math.pi*2)
FONTCOLOR = (255,255,255)   # colore delle scritte
FONTNAME = 'Consolas'
BG_IMAGE = 'IMMAGINI'+ bars + 'background.png'
CHOICE_IMAGE = 'IMMAGINI'+ bars + 'mushroom.png'
P1_IMAGE = 'IMMAGINI'+ bars + 'mario.png'
P2_IMAGE = 'IMMAGINI'+ bars + 'peach_r.png'
MELA_IMG = 'IMMAGINI'+ bars + 'mela.png'
BOWSER_IMG = 'IMMAGINI' + bars + 'bowser.png'
GAME_OVER_IMG = 'IMMAGINI'+ bars + 'gameover.png'
GAME_OVER_SOUND = 'MUSIC'+ bars + 'smb_gameover.wav'
MELA_HIT_SOUND = 'SFX'+ bars + 'smb_coin.wav' #suono alla collisione con la mela
MARIO_JUMP_SOUND = 'SFX'+ bars + 'marioJump.mp3'
MAIN_THEME = 'MUSIC'+ bars + 'maintheme.ogg'
DB_PATH_NAME = 'DB'
SCORE_DB_FILE = 'scores.db'
#################################################
