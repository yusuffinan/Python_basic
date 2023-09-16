bakiye = 1000
while True:

    a = int(input("yapmak istediğiniz işlemi seçin\n 1: para yatırma, 2: para çekme, 3 bakiye sorgulama, çıkış 4"))
    if a ==1:
        money= int(input("miktar girin"))
        
        bakiye += money
        print(f"{bakiye} --- güncel bakiye")
        
    elif a == 2:
        moneyy= int(input("miktar girin"))
        if bakiye-moneyy < 0:
            print("bunu seçemezsin")
            continue
        bakiye -= moneyy
        print(f"{bakiye} --- güncel bakiye")
        
    elif a == 3:
        print("bakiye", bakiye)
    elif a == 4:
        break
    else: 
        print("geçersiz")
