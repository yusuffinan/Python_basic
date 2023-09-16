a = int(input("sayi"))
s =0
sayi = str(a)
for item in sayi:
    
    c = int(item)  ** len(sayi)
    s = s+ c
    
if s == a:
    print("oldu")
else:
    print("olmadı")
print(s)