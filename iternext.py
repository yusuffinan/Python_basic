class kareler():
    def __init__(self, maks = 0):
        self.sayi =1
        self.maks = maks
    def __iter__(self):
        return self
    def __next__(self):
        if self.sayi <= self.maks:
            print(self.sayi**2)
        else:
            raise StopIteration
        self.sayi +=1

ka = kareler(5)
k = iter(ka)

for i in ka:
    next(k)