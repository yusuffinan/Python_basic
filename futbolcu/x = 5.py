fb =[]
gs = []
bjk = []
with open("futbolcular.txt","r",encoding="utf-8") as file:
    liste = file.readlines()
    print(liste)
    
   
    for i in liste:
        i = i[:-2]
        satir = i.split(",")
        if (satir[1]) == " fenerbahçe":
            fb.append(i)
        elif (satir[1]) == " galatasaray":
            gs.append(i)
        elif (satir[1]) == " beşiktaş":
            bjk.append(i)
            
        


with open("fb.txt","w",encoding="utf-8") as fb1:
    for ad in fb:
         fb1.write(ad +"\n")
fb1.close()
with open("gs.txt","w",encoding="utf-8") as gs1:
    for ad in gs:
        gs1.write(ad +"\n")
with open("bjk.txt","w",encoding="utf-8") as bjk1:
    for ad in bjk:
        bjk1.write(ad +"\n")