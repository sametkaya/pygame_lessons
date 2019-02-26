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

gameDisplay.fill(white) #ekranı her framede tekrar çizdiriyoruz

myimage = pygame.image.load("Dead (1).png")
myimage= pygame.transform.scale(myimage, (200, 200)) #resmi yeniden boyutlandırma
imagerect = myimage.get_rect() #resmin çerçevesi
gameDisplay.blit(myimage, imagerect) #resmin çizimi
#gameDisplay.blit(myimage, [100,100,100,100])#bu şekilde de olabilir.

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True


    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()
