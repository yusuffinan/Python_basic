class personel():
    def __init__(self,ad,soyad,numara,maas, diller):
        self.ad = ad
        self.soyad = soyad
        self.numara = numara
        self.maas = maas
        self.diller = diller
    def bilgi(self):
        print(f"""
              ad: {self.ad}
              soyad: {self.soyad}
              numara: {self.numara}
              maas: {self.maas}
              diller: {self.diller}
""")
    def zam(self,zam_miktar):
            self.maas += zam_miktar
            print("zam yapıldı")
    def yenidil(self,new_lng):
         print("yeni dil ekleniyor")
         self.diller.append(new_lng)
yusuf = personel("yusuf","inan",147,25000,["python","SQL"])
yusuf.bilgi()
yusuf.zam(1500)
yusuf.yenidil("C#")
yusuf.bilgi()
print(yusuf.diller)