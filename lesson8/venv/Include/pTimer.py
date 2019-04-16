import time
from  threading import Timer
class pTimer():
    #bu sınıf timer kullanılarak tarasarlanmıştır.
    #timer aslında bir threadtir.
    #ancak pythonda sonsuz çalışma göstermez bu yüzden böyle bir sınıfa ihtiyaç duyduk.
    #başlangıç fonksiyonu tekrar zamanı, çalıştıırlacak fonksiyon ve varsa arguman alır.
    def __init__(self,interval,handlerFunction,*arguments):
        self.interval=interval
        self.handlerFunction=handlerFunction
        self.arguments=arguments
        self.running=False
        self.timer=Timer(self.interval,self.run,arguments)
        self.isPause=False
    #işlemi başlatma fonsiyonu
    def start(self):
        self.running=True
        self.timer.start()

    #bitirme fonksiyonu
    def stop(self):
        self.running=False

    def pause(self,status=False):
        self.isPause=status

    #sürekli çalışacak olan fonksiyonu
    def run(self,*arguments):
        #stop olana kadar sozsuz döngü
        while self.running:
            #çalışacak fonsiyonu çağırıyoruz
            self.handlerFunction(arguments)
            #timerı uyutma süresi
            time.sleep(self.interval)
            while self.isPause:
                time.sleep(0.10)
                continue


