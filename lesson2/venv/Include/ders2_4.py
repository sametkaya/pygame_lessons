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


clock = pygame.time.Clock()


gameDisplay.fill(white)
x=int(gameDisplay.get_width()/2)-50
y=int(gameDisplay.get_height()/2)-50
xp=int(gameDisplay.get_width()/2)-50
yp=int(gameDisplay.get_height()/2)-50
xn=int(gameDisplay.get_width()/2)-50
yn=int(gameDisplay.get_height()/2)-50

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

    gameDisplay.fill(white) #ekranı her framede tekrar çizdiriyoruz
    pygame.draw.rect(gameDisplay, red, [xp,y,100,100]) #şekil herseferinde yeni konumunda çiziliyor
    pygame.draw.rect(gameDisplay, blue, [x,yp,100,100]) #şekil herseferinde yeni konumunda çiziliyor
    pygame.draw.rect(gameDisplay, green, [xn,y,100,100]) #şekil herseferinde yeni konumunda çiziliyor
    pygame.draw.rect(gameDisplay, black, [x,yn,100,100]) #şekil herseferinde yeni konumunda çiziliyor
    xp=xp+1
    yp=yp+1
    xn=xn-1
    yn=yn-1

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()
