def deco(func):
    def wrapper(sayilar):
        ciftort =0
        tekort= 0
        teks = 0
        cifts= 0
        for j in sayilar:
            if j % 2 == 0:
                cifts +=1
                ciftort += j
            else:
                teks += 1
                tekort += j
        print(func.__name__ + "tek sayıların ortalaması", (tekort/teks), "cift sayilarin ortalaması ", (ciftort/cifts))
    return wrapper

@deco
def ortalama(sayilar):
    toplam = 0
    for i in sayilar:
        toplam += i
    print("ortalaması genel", (toplam/len(sayilar)))
ortalama([1,5,6,7,8,99,51,66])