def bul(a,b):
    if a > b:
        c = a
    else:
        c = b

    for i in range(1,c+1):
        if a % i == 0 and b% i==0:
            ebob = i
    print("ekok", (a*b) // ebob)
    return ebob
    
a = int(input("ilk sayi"))
b = int(input("ikinci sayi"))
print("ebobe:", bul(a,b))


        