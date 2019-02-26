import pygame
import sys

pygame.init()
gameDisplay_width=800
gameDisplay_height=600
gameDisplay = pygame.display.set_mode((gameDisplay_width,gameDisplay_height))
pygame.display.set_caption('Gamemaker')

crashed = False

clock = pygame.time.Clock()

while not crashed:
    for event in pygame.event.get(): #olaylar listesi
        if event.type == pygame.QUIT:
            crashed = True
        print(event) #oalyları yazdırıyoruz
        print(event.type) #oaly tipleri

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()
