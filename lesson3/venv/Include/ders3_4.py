import pygame
import sys

pygame.init()
gameDisplay_width=800
gameDisplay_height=600
gameDisplay = pygame.display.set_mode((gameDisplay_width,gameDisplay_height))
pygame.display.set_caption('Gamemaker')

crashed = False

white = (255, 255,255)
black = (0,0,0)
blue =  (0,0,255)


clock = pygame.time.Clock()



x=30
y=30
mx=0 #x haraket yönü
my=0 #y haraket yönü

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        if event.type == pygame.MOUSEMOTION:
            #çizimin mouse ile haraketi için mouse posizyon değerlini alıyoruz.
            #x ve y kordinasyonlarını set ediyoruz
            mouse_position = pygame.mouse.get_pos()
            x=mouse_position[0]
            y=mouse_position[1]

    gameDisplay.fill(white)
    pygame.draw.rect(gameDisplay, blue, [x,y,100,100])


    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()
