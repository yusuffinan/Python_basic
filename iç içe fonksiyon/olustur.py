def to(*args, **kwargs):
    for i in args:
        print(i)
    for j,k in kwargs.items():
        print(j,k)
#to(4,5,6,7, isim = ": yusuf", soyad= ": inan")
def ilk():
    def ikinci():
        print("küçükten selam")
    ikinci()
    print("büyükten selam")

def topla(*args):
    def toplam(args):
        toplama =0
        for i in args:
            toplama += i
        print(toplama)
    toplam(args)
topla(4,5,6)

