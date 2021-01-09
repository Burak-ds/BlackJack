import pandas as pd
import random
from termcolor import colored, cprint
import time
print("********************")
text1 = colored('WELCOME TO BlackJack', 'blue', attrs=['reverse', 'blink'])
print(text1)
print("********************")
print("""
***********
Kart Çekmek İçin 1'e basın
Kart İstemiyorsanız 2'ye basın.
""")
kart_listesi = [1,2,3,4,5,6,7,8,9,10,10,10,10,11]
kasa = 0
oyuncu = 0
#Oyuncunun Turu
while oyuncu<=21:
    order = input("Emir Giriniz( 1 / 2 ):")
    if (float(order) == 1):
        rast = random.randint(0,13)
        gelen_sayı = kart_listesi[rast]
        oyuncu += gelen_sayı
        print("Çektiğiniz kart: {}".format(gelen_sayı))
        print(colored("Skorunuz:{}".format(oyuncu),'blue'))
        continue
    else:
        Oyuncu_Total = oyuncu
        print("Skorunuz: {} ".format(Oyuncu_Total))
        break
if oyuncu > 21:
    print(colored("Kaybettiniz",'red'))
#Kasanın Turu
while (oyuncu <=21 and kasa<=21):
    if kasa == 21 & oyuncu <=21:
        print(colored("Kaybettiniz",'red'))
        break

    rast = random.randint(0, 13)
    kasaya_gelen_sayı = kart_listesi[rast]
    kasa += kasaya_gelen_sayı
    print("Kasanın çektiği kart: {}".format(kasaya_gelen_sayı))
    print(colored("Kasa skoru:{}".format(kasa),'red'))
    time.sleep(1)
    if kasa > oyuncu:
        break

if (kasa > 21 and oyuncu<=21):
    print(colored("KASA TOPLAMI:{}".format(kasa), 'blue'))
    print(colored("Sizin Toplamınız:{}".format(oyuncu),'blue'))
    print(colored("Kazandınız",'green'))

while (oyuncu<=21 and kasa <=21):
    if kasa > oyuncu:
        print(colored("Kasa Toplam: {}".format(kasa),'blue'))
        print(colored("Oyuncu Toplam:{}".format(oyuncu),'blue'))
        print(colored("KAYBETTİNİZ",'red'))
        break
    elif kasa==oyuncu:
        print(colored("Kasa Toplam: {}".format(kasa),'blue'))
        print(colored("Oyuncu Toplam:{}".format(oyuncu),'blue'))
        print(colored("BERABERE",'yellow'))
        break
    else:
        print(colored("Kasa Toplam: {}".format(kasa),'blue'))
        print(colored("Oyuncu Toplam:{}".format(oyuncu),'blue'))
        print(colored("KAZANDINIZ",'green'))
        break
