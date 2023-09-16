import time
def fo(func):
    def wrapper(sayi):
        baslangic = time.time()
        sonuc = func(sayi)
        bitis = time.time()
        print(sonuc)
        print(str(bitis-baslangic))
    return wrapper

@fo
def topla(sayi):
    time.sleep(1)
    toplam = 0
    for i in sayi:
        toplam += i
    return toplam
liste =[1,5,6,4]
sonuc = topla(liste) 
