def hesp():
    liste=[] 
    for i in range(1,100):            
        for j in range(1,100):
           for k in range(1,100):
                if (i **2 == j**2 + k**2):
                   liste.append((j,k,i))
    return liste
print(hesp())
