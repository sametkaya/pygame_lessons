#çizim ile işlemler yapabilsek dahi kontrol için objelere ihtiyacımız vardır.
#bu noktada object merkezli programlama yapmamız gerekir.
import pygame
import sys
import math
import random
from Player import Player
class Game():
    endEvent=pygame.event.Event(pygame.USEREVENT, attr1='endEvent')
    
    def __init__(self):
        
        pygame.init()
        self.gameDisplay_width=900
        self.gameDisplay_height=600
        self.gameDisplay = pygame.display.set_mode((self.gameDisplay_width,self.gameDisplay_height))
        pygame.display.set_caption('Sıbcıkrık')
        self.backGroundImage=pygame.transform.scale(pygame.image.load("images/BG.png"),(self.gameDisplay.get_width(), self.gameDisplay.get_height()))
        self.end = False
        self.clock = pygame.time.Clock()
        self.player1= Player(self.gameDisplay)
        
        
        
    def start(self):
        self.player1.start()
        while not self.end:
        
            for event in pygame.event.get():
        
                if event.type == pygame.QUIT:
                    self.end = True
                elif event== Game.endEvent:
                    self.end = True
                    break
                elif event.type==pygame.KEYDOWN:
                    self.player1.key_down(event.key)
                elif event.type==pygame.KEYUP:
                    self.player1.key_up(event.key)
                    
            self.gameDisplay.blit(self.backGroundImage,(0,0))        
            self.player1.draw()
            pygame.display.update()
            self.clock.tick(60)
        
        pygame.quit()
        quit()

