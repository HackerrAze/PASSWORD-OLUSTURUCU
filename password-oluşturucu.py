from random import choice
import os,time
os.system('clear')

def güncelle():
    os.system("""
    cd ..
    rm -rf PASSWORD-OLUSTURUCU
    git clone https://github.com/HackerrAze/PASSWORD-OLUSTURUCU
    cd PASSWORD-OLUSTURUCU
    chmod +x password-oluşturucu.py
    python password-oluşturucu.py
    """)
    
gün = input("Toolsu Güncellemek İstiyormusun? [E/h] ")

if gün == "E" or gün == "e":
    güncelle()
    exit()

h1 = "qwertyuiopasdfghjklzxcvbnm"
h2 = h1.upper()
h3 = "1234567890"

lis = []

for i in h1,h2,h3:
    lis += str(i)
try:
    sayı = int(input("Sayı Giriniz: "))
except Exception:
    print("\nSayı Giriniz!")
    exit()

sifre = ""
if sayı >=8 and sayı <=64:
    for j in range(sayı):
        sifre += str(choice(lis))
    print("\n Şifre Oluşturuluyor...")
    time.sleep(3)
    print("\n"+">"*59)
    print("\nOLUŞTURULAN ŞİFRE: ",'\33[32m'+sifre+"\n"+'\33[37m')
    print(">"*59)
    exit()
elif sayı < 8:
    print("\n8'den Küçük Sayı Olamaz!")
    exit()
elif sayı > 64:
    print("\n64'den Büyük Sayı Olamaz!")
    exit()








