def hsp():
    for i in range(1,6):
        yield(i**2)
d=hsp()
c = iter(d)
print(next(c))
print(next(c))

