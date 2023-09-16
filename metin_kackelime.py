class dosya():
    def __init__(self):
        with open("metin.txt","r",encoding="utf-8") as file:
            metin = file.read()
            kelimeler = metin.split()
            self.s = list()
            for i in kelimeler:
                i =i.strip("\n")
                i = i.strip(" ")
                i= i.strip(".")
                i = i.strip(",")
                self.s.append(i)
            
    def tum(self):
        tumu = set()
        for a in self.s:
            tumu.add(a)
        print(tumu)
        for c in tumu:
            print(c)
    def frekans(self):
        kacvar = dict()
        for i in self.s:
            if (i in kacvar):
                kacvar[i] += 1
            else:
                kacvar[i] = 1
        for kelime, sayi in kacvar.items():
            print(f"{kelime} kelimesinden {sayi} adet varmış")


d=dosya()
d.tum()
d.frekans()