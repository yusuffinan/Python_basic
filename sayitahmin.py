import random
import time

rastgele= random.randint(1,40)
hak = 5
while True:
    a = int(input("sayi"))
    hak -= 1
    if a == rastgele:
        print("tebrikler bildiniz sayi", rastgele)
        break
    elif a< rastgele:
        time.sleep(1)
        print("daha büyük girin")
    else:
        time.sleep(1)
        print("küçük girin")
    if hak ==0:
        print("hakkınız kalmamıştır")
        break
print("sayi",rastgele)