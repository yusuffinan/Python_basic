dic = ["boş","on","yirmi","otuz","kırk","elli","altmış","yetmiş","seksen","doksan"]
sayi = ["sıfır","bir","iki","üç","dört","beş","altı","yedi","sekiz","dokuz"]


def bul(a):
    birinci = int(b[0])
    ikinci = int(b[1]) 
    print(f"{dic[birinci]} {sayi[ikinci]}")

a = input("sayıyı alalım")
b = list(a)
bul(b)

       #         |
#alternatif ->   v
"""
birler =  ["","Bir","İki","Üç","Dört","Beş","Altı","Yedi","Sekiz","Dokuz"]
onlar = ["","On","Yirmi","Otuz","Kırk","Elli","Altmış","Yetmiş","Seksen","Doksan"]
def okunus(sayı):
    birinci = sayı % 10
    ikinci = sayı // 10
    
    return onlar[ikinci] + " " + birler[birinci]

    
sayı =  int(input("Sayı:"))

print(okunus(sayı))
"""