"""
toplam = 0
a =1
b =1
for tablo in range(10):
    for basamak in range(9):
        toplam = a * b
        print(f"{b} x {a} = {toplam}")
        a+=1
        if a == 10:
            a =1
    b+=1
    """

for i in range(1,11):
    for j in range(1,11):
        print("{} x {} = {}".format(i,j, i*j))