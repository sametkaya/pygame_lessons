import pygame
import sys

pygame.init()
gameDisplay_width=800
gameDisplay_height=600
gameDisplay = pygame.display.set_mode((gameDisplay_width,gameDisplay_height))
pygame.display.set_caption('Gamemaker')

crashed = False

white = (255, 255,255)



clock = pygame.time.Clock()


gameDisplay.fill(white)
x=int(gameDisplay.get_width()/2)
y=int(gameDisplay.get_height()/2)
radius=10
r=0
g=0
b=0
while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True


    pygame.draw.circle(gameDisplay, (r,g,b), [x,y],radius,2) #şekil her seferinde yeni çapla çizdirilioyor.
    radius=radius+3
    r=(r+5)%255 # rgb renkler 0-255 arası renk alır.
    g=(g+15)%255 # bundan dolayı mod 255 yapıyoruz.
    b=(b+20)%255 #r g b hepsi aynı artsa 5 5 5 gibi gri skala renkler çıkar

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()
