def topla(a,b):
    return(a+b)
def cikar(a,b):
    return(a-b)
def carp(a,b):
    return(a*b)
def bol(a,b):
    return(a/b)

def ana(f1,f2,f3,f4,islem):
    if islem == "topla":
        print(f1(4,4))
    if islem == "cikar":
        print(f2(4,4))
    if islem == "carp":
        print(f3(4,4))
    if islem == "bol":
        print(f4(4,4))
ana(topla,cikar,carp,bol,"bol")
