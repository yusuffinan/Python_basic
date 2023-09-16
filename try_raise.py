liste = [1,2,3,4,5,6,7,8]
def ct(s):
    if s % 2 == 0:
        return s
    else:
        raise ValueError("bu sayı tek")

for i in liste:
    try:
        if i % 2 ==0:
           print(ct(i))
    except ValueError:
        print("hataa")