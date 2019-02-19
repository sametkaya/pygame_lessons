import pygame #pygame kütüphanesini ekliyoruz
import sys

pygame.init() #tüm pygame modüllerini başlatıyor

gameDisplay = pygame.display.set_mode((800,600)) # tasarlanacak ekran boyutu
pygame.display.set_caption('Gamemaker') #ekran başlığı
crashed = False


#oyunu bitime kadar sonsuz döngüye sokuyoruz
while not crashed:

    for event in pygame.event.get(): #oluşmuş olan olayları tarıyoruz
        if event.type == pygame.QUIT: #olay tipine göre karar mekanizmalarını kuruyoruz
            crashed = True # çıkış durumunda döngüyü kırar
            #break         komutuda kullanılabilir mi?

        print(event) #olayı ekrana yazdırıyoruz

    pygame.display.update() #her döngüde ekranı tekrar çizdiriyoruz

pygame.quit()
quit()
