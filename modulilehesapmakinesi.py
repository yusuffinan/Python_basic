import modul
while True:
    a = input("işlem ne")
    print("iki adet sayı giriniz")
    sayi1= int(input("sayi1"))
    sayi2= int(input("sayi2"))
    if a == "topla":
       print(modul.topla(sayi1,sayi2))
    elif a == "cikar":
        print(modul.cikar(sayi1,sayi2))
    elif a == "carp":
       print(modul.carp(sayi1,sayi2))
    elif a == "bol":
       print(modul.bol(sayi1,sayi2))
    elif a == "kapat":
       print("döngü bitti")
       break