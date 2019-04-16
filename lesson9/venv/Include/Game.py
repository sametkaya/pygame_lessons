#çizim ile işlemler yapabilsek dahi kontrol için objelere ihtiyacımız vardır.
#bu noktada object merkezli programlama yapmamız gerekir.
import pygame
import sys
import math
import random

class Game():
    endEvent=pygame.event.Event(pygame.USEREVENT, attr1='endEvent')
    
    def __init__(self):
        
        pygame.init()
        
        self.gameDisplay_width=800
        self.gameDisplay_height=600
        self.gameDisplay = pygame.display.set_mode((self.gameDisplay_width,self.gameDisplay_height))
        pygame.display.set_caption('Sıpcık')
        
        self.end = False
        
        self.clock = pygame.time.Clock()
        
        
    def start(self):
        
        while not self.end:
        
            for event in pygame.event.get():
        
                if event.type == pygame.QUIT:
                    self.end = True
                elif event== Game.endEvent:
                    self.end = True
                    break
                    
            pygame.display.update()
            self.clock.tick(60)
        
        pygame.quit()
        quit()

