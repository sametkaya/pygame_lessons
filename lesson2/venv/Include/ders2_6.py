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
backGraundImage=pygame.image.load('BG.png')
backGraundImage= pygame.transform.scale(backGraundImage, (gameDisplay_width, gameDisplay_height)) #resmi yeniden boyutlandırma


haraket=1;
while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

    gameDisplay.blit(backGraundImage, (0, 0))
    myimage = pygame.image.load("Dead ("+str(haraket)+").png") #resim yükleme yolunu belirtiyoruz
    imagerect = myimage.get_rect()
    gameDisplay.blit(myimage, imagerect)
    haraket=(haraket+1)%12+1# 12 resim var
    pygame.display.update()
    pygame.time.delay(100)# 100 milisaniye bekleme süresi veriyoruz
    clock.tick(60)

pygame.quit()
quit()
