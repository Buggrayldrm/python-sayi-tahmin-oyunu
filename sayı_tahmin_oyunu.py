print("""
SAYI TAHMİN OYUNU
1 ile 100 arasında tahmininizi yapınız...
""")

import random
import time

rastgele_Sayı = random.randint(1,100)
giriş_hakkı =7
while True:
    sayı = int(input("Sayınızı giriniz:"))
    if sayı < rastgele_Sayı:
        print("Bilgiler sorgulanıyor...")
        time.sleep(2)
        print("Daha yüksek bir sayı tahmin ediniz...")
        giriş_hakkı -=1
    elif sayı >rastgele_Sayı:
        print("Bilgiler sorgulanıyor...")
        time.sleep(2)
        print("Daha düşük bir sayı tahmin ediniz...")
        giriş_hakkı -=1
    else:
        print("Bilgiler sorgulanıyor...")
        time.sleep(2)
        print("Tebrikler! Doğru tahmin.. SAYI:",rastgele_Sayı)
        break
    if  giriş_hakkı == 0:
        print("Giriş hakkınız bitmiştir...")
        break