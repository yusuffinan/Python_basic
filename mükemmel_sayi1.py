def bul(a):
    toplam =0
    for i in range(1,a):
        if a % i == 0:
         toplam += i
    if toplam == a:
        return("mükemmel sayi")
    else:
        return("mükemmel sayi değil")
print(bul(28))