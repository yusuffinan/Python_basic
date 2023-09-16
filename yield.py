def kare():
    for i in range(1,16):
        yield(i**2)

geno = kare()
geno = iter(geno)
for i in range(5):
    print(next(geno))

ist = (i * 3 for i in range(1,4))
print(ist)
g = iter(ist)
#print(next(g))

def tablo():
    for i in range(1,11):
        for j in range(1,11):
            yield f"{i,j},  = {i*j}"
dd = tablo()
dc = iter(dd)
print(next(dc))
for i in tablo():
    print(i)