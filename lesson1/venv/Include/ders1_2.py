import pygame #pygame kütüphanesini ekliyoruz
import sys

pygame.init() #tüm pygame modüllerini başlatıyor

gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption('Gamemaker')
crashed = False

clock = pygame.time.Clock() #zamanlama için bir clock tanımlıyoruz

while not crashed:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        print(event)

    pygame.display.update() #her döngüde ekranda güncellenen bir şey varsa ekranı tekrar çizdiriyoruz
    clock.tick(60)
    #sonsuz döngü çok hızlı döner. ancak insan gözü saniyede ancak 30 frame görebilir.
    #bunun iyileştirilmiş hali 60 framedir. frame yenilenme oranına fps(frame per second) denir.
    #burada saniyede 60 framelik bir yenilenme olacak demektir.
    print(clock.get_time()) #zamanı yazdırıyoruz
    print(clock.get_fps()) #frame oranını yazdırıyoruz
    
pygame.quit()
