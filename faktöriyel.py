a = int(input("sayı gir"))
while a>0: 
    nm= 1
    for i in range(a):
        nm *=a
        a -=1
        print("işlem", nm, "sayi: ", a)
    print("sonç:",nm)
