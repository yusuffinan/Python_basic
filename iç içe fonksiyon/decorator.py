import time
def zaman(func):
    def wrapper(sayilar):
        baslangic = time.time()

        sonuc = func(sayilar)

        bitis = time.time()
        print(func.__name__ + " baslangic ile bitiş arasındaki fark" + str(bitis - baslangic))
        return sonuc
    return wrapper


@zaman
def kare(sayilar):
    sonuc = []
    time.sleep(1)
    for i in sayilar:
        sonuc.append(i**2)
    return sonuc

@zaman
def kup(sayilar):
    sonuc = []
    time.sleep(1)

    for i in sayilar:
        sonuc.append(i**3)
    return sonuc
kare(range(1000))
kup(range(1000))
