def islem(islem_ne):
    def toplama(*args):
        toplam = 0
        for i in args:
            toplam += i
        print(toplam)
    
    def carpım1(*args):
        carpım = 1
        for j in args:
            carpım *= j
        print(carpım)
    if islem_ne == "toplam":
        return(toplama)
    elif islem_ne == "carpım":
        return(carpım1)
fonk = islem("toplam")
fonk2 = islem("carpım")
fonk(1,4,5,6)
fonk2(1,4,5,6)
