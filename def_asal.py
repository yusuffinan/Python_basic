def asal(s):
    i = 1
    t=0
    while i <= s:
        if s % i ==0:
            t += 1
        i+= 1
    if t !=2:
        print("asal değil")
    else:
        print("asal")

asal(12)