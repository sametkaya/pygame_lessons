#çizim ile işlemler yapabilsek dahi kontrol için objelere ihtiyacımız vardır.
#bu noktada object merkezli programlama yapmamız gerekir.
import pygame
import sys
import math
import random
from Chapter import ChapterOne

pygame.init()

gameDisplay_width=800
gameDisplay_height=600
gameDisplay = pygame.display.set_mode((gameDisplay_width,gameDisplay_height))
pygame.display.set_caption('Gamemaker')

crashed = False

clock = pygame.time.Clock()
chapter= ChapterOne(gameDisplay)
chapter.start(gameDisplay)
endEvent=pygame.event.Event(pygame.USEREVENT, attr1='endEvent')

end=False
while not crashed:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            crashed = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                chapter.plane.my=-1
            if event.key == pygame.K_DOWN:
                chapter.plane.my=1
            if event.key == pygame.K_LEFT:
                chapter.plane.mx=-1
            if event.key == pygame.K_RIGHT:
                chapter.plane.mx=1
            if event.key == pygame.K_SPACE:
                chapter.plane.fire(gameDisplay)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                chapter.plane.my=0
            if event.key == pygame.K_DOWN:
                chapter.plane.my=0
            if event.key == pygame.K_LEFT:
                chapter.plane.mx=0
            if event.key == pygame.K_RIGHT:
                chapter.plane.mx=0
        #event karşılaştırmalarında eşitlik koşulu çalışır
        #eventlar aynı olmalı özellikleriyle birlikte
        elif event== chapter.finishEvent:
            print(event)
            end=True

        elif event== chapter.plane.exposedEvent:
            print(event)
    if not end:
        chapter.draw(gameDisplay)


    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()

