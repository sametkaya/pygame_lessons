import pygame
import sys

pygame.init()
gameDisplay_width=800
gameDisplay_height=600
gameDisplay = pygame.display.set_mode((gameDisplay_width,gameDisplay_height))
pygame.display.set_caption('Gamemaker')

crashed = False

black = (0,0,0)
white = (255, 255,255)
blue =  (0,0,255)
green = (0,255,0)
red =   (255,0,0)
colorList=[black,blue,green,red] # renk listesi oluşturuyoruz


clock = pygame.time.Clock()



x=30
y=30
color=0

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
        if event.type == pygame.MOUSEBUTTONDOWN:
            color=(color+1)%len(colorList) #mouse tıklamasıyla renk değişimi yapılıyor.
    gameDisplay.fill(white)
    pygame.draw.rect(gameDisplay, colorList[color], [x,y,100,100])


    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()
