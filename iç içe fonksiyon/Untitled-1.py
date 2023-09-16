def sonucagit(*args):
    def topla(args):
        toplam = 0
        for i in args:
            toplam += i
        print(toplam)
    topla(args)
sonucagit(4,5,6)