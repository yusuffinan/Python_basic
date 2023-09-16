def muk(func):

    def wrapper():
        print("mükemmel sayı hesaplanıyor")     
        for j in range(1,1000):
            toplam = 0
            for i in range(1,j):
                if j % i == 0:
                    toplam+= i
            if (toplam == j):
                print(j, "mükemmel sayi")
        func()
    return wrapper

@muk
def asal():
    for j in range(1,1000):
        i = 1
        t = 0
        while i <= j:
            if j % i == 0:
                t += 1
            i+=1
        if t != 2:
            pass
        else: 
            print(j, "asal")
asal()